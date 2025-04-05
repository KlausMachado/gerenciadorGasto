import csv
import os
from datetime import datetime

# Nome do arquivo CSV
arquivo_csv = 'dados_financeiros.csv'

# Função para validar o formato da data
def validar_data(data):
    try:
        datetime.strptime(data, '%d-%m-%Y')
        return True
    except ValueError:
        return False

# Função para carregar os dados do arquivo CSV
def carregar_dados():
    if not os.path.exists(arquivo_csv):
        print("Arquivo vazio.")
        return []
    with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Função para salvar os dados no arquivo CSV
def salvar_dados(dados):
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['data', 'descricao', 'parcela_atual', 'total_parcelas', 'valor', 'categoria', 'banco']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dados)

# Função para adicionar um novo registro
def adicionar_registro():
    while True:
        data = input("Data (DD-MM-YYYY): ")
        if validar_data(data):
            break
        print("Formato de data inválido! Use DD-MM-YYYY.")
    
    descricao = input("Descrição: ")
    total_parcelas = int(input("Número total de parcelas: "))
    if  total_parcelas == 0:
        parcela_atual = 1
    else:    
        parcela_atual = int(input(f"Qual a parcela atual (1 a {total_parcelas}): "))
    print(f"Utilize (.) para separar as casas decimais.")    
    valor = float(input("Valor: "))
    categoria = input("Categoria: ").upper().strip()
    banco = input("Banco: ").upper().strip()
    
    novo_registro = {
        'data': data,
        'descricao': descricao,
        'parcela_atual': parcela_atual,
        'total_parcelas': total_parcelas,
        'valor': valor,
        'categoria': categoria,
        'banco': banco
    }
    
    dados = carregar_dados()
    dados.append(novo_registro)
    salvar_dados(dados)
    print("Registro adicionado com sucesso!")

# Função para listar todos os registros
def listar_registros():
    dados = carregar_dados()
    if not dados:
        print("Nenhum registro encontrado.")
        return
    
    for i, registro in enumerate(dados):
        print(f"----------------------------------------- \nRegistro {i}:")
        print(f"Data: {registro['data']}")
        print(f"Descrição: {registro['descricao']}")
        print(f"Parcela: {registro['parcela_atual']} de {registro['total_parcelas']}")
        print(f"Valor: R$ {float(registro['valor']):.2f}")
        print(f"Categoria: {registro['categoria']}")
        print(f"Banco: {registro['banco']}")
        print("------------------------------------------")
        
# Função para ordenar registros por data ou valor
def ordenar_registros():
    print("\nOrdenar registros por:")
    print("1. Data")
    print("2. Valor")
    opcao = input("Escolha uma opção: ")
    
    dados = carregar_dados()
    
    if opcao == '1':
        # Ordenar por data
        dados_ordenados = sorted(dados, key=lambda x: datetime.strptime(x['data'], '%d-%m-%Y'))
        print("\nRegistros ordenados por data:")
    elif opcao == '2':
        # Ordenar por valor
        dados_ordenados = sorted(dados, key=lambda x: float(x['valor']))
        print("\nRegistros ordenados por valor:")
    else:
        print("Opção inválida!")
        return
    
    for i, registro in enumerate(dados_ordenados):
        print(f"----------------------------------------- \nRegistro {i}:")
        print(f"Data: {registro['data']}")
        print(f"Descrição: {registro['descricao']}")
        print(f"Parcela: {registro['parcela_atual']} de {registro['total_parcelas']}")
        print(f"Valor: R$ {float(registro['valor']):.2f}")
        print(f"Categoria: {registro['categoria']}")
        print(f"Banco: {registro['banco']}")
        print("------------------------------------------")
        

# Função para alterar um registro
def alterar_registro():
    dados = carregar_dados()
    if not dados:
        print("Nenhum registro encontrado.")
        return
    #for i, registro in enumerate(dados):
        #print(f"\nRegistro {i}: {registro['descricao']}")
    try:
        indice = int(input("Digite o índice do registro que deseja alterar: "))
    except ValueError:
        print("Índice inválido! Digite um número inteiro.")
        return
    try:   
        if 0 <= indice < len(dados):
            print(f"Editando registro: {dados[indice]['descricao']}")
            while True:
                nova_data = input("Nova data (DD-MM-YYYY): ")
                if validar_data(nova_data):
                    break
                print("Formato de data inválido! Use DD-MM-YYYY.")
        
            dados[indice]['data'] = nova_data
            dados[indice]['descricao'] = input("Nova descrição: ")
            dados[indice]['total_parcelas'] = int(input("Novo total de parcelas: "))
            if dados[indice]['total_parcelas'] == 0:
                    dados[indice]['parcela_atual'] = 1
            else:    
                dados[indice]['parcela_atual'] = int(input("Nova parcela atual: "))
          
            dados[indice]['valor'] = float(input("Novo valor: "))
            dados[indice]['categoria'] = input("Nova categoria: ").upper().strip()
            dados[indice]['banco'] = input("Novo banco: ").upper().strip()
        
            salvar_dados(dados)
            print("Registro alterado com sucesso!")
        else:
            print("Índice inválido!")
    except ValueError:
        print("Índice inválido! Digite um número inteiro.")
        return                       

# Função para deletar um registro
def deletar_registro():
    listar_registros()
    try:
        indice = int(input("Digite o índice do registro que deseja deletar: "))
    except ValueError:
        print("Índice inválido! Digite um número inteiro.")
        return
    
    dados = carregar_dados()
    
    if 0 <= indice < len(dados):
        print(f"\nDeletando registro: {indice} - {dados[indice]['descricao']}")
        confirmacao = input("Tem certeza que deseja deletar este registro? (s/n): ").strip().lower()
        if confirmacao == 's':
            dados.pop(indice)
            salvar_dados(dados)
            print("Registro deletado com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Índice inválido!")        

# Função para filtrar registros por categoria
def filtrar_por_categoria():
    dados = carregar_dados()
    
    if not dados:
        print("Nenhum registro encontrado.")
        return
    
    #coleta categorias unicas dos registros
    categorias_disponiveis = set(registro['categoria'] for registro in dados)
    
    if not categorias_disponiveis:
        print("Nenhuma categoria encontrada.")
        return

    #exibir categorias disponiveis
    print("\nCategorias disponiveis:")
    for categoria in categorias_disponiveis:
        print(f"- {categoria}")                
            
    categoria = input("Digite a categoria para filtrar: ").upper().strip()    
    filtrados = [registro for registro in dados if registro['categoria'] == categoria]
    
    if not filtrados:
        print("Nenhum registro encontrado para essa categoria.")
        return
    
    valor_total = 0
    for registro in filtrados:
        print(f"\nData: {registro['data']}")
        print(f"Descrição: {registro['descricao']}")
        print(f"Parcela: {registro['parcela_atual']} de {registro['total_parcelas']}")
        print(f"Valor: R$ {float(registro['valor']):.2f}")
        print(f"Categoria: {registro['categoria']}")
        print(f"Banco: {registro['banco']}")
        print("-----------------------------------------------------")
        valor_total += float(registro['valor'])

    print(f"--------\nValor total para a categoria '{categoria}': R${valor_total:.2f}\n----------")        

def filtrar_por_banco():
    dados = carregar_dados()        
    banco = input("Digite o banco para filtrar: ").upper().strip()    
    filtrados = [registro for registro in dados if registro['banco'] == banco]
    
    if not filtrados:
        print("Nenhum registro encontrado para esse banco.")
        return
    
    valor_total = 0
    for registro in filtrados:
        print(f"\nData: {registro['data']}")
        print(f"Descrição: {registro['descricao']}")
        print(f"Parcela: {registro['parcela_atual']} de {registro['total_parcelas']}")
        print(f"Valor: R$ {float(registro['valor']):.2f}")
        print(f"Categoria: {registro['categoria']}")
        print(f"Banco: {registro['banco']}")
        print("-----------------------------------------------------")
        valor_total += float(registro['valor'])

    print(f"--------\nValor total para o banco '{banco}': R${valor_total:.2f}\n----------")        


# Função para calcular o valor total de todos os registros
def calcular_valor_total():
    dados = carregar_dados()
    total = sum(float(registro['valor']) for registro in dados)    
    renda = float(input("Digite foi o valor da sua renda no mes: "))
    
    print("-----------------------------------------------------")
    print(f"Valor total de todos os registros: R$ {total:.2f}")
    print("-----------------------------------------------------")
    print(f"Valor fatura - renda = {(renda - total):.2f}")
    print("-----------------------------------------------------")    

# Função para calcular o valor total por categoria
def calcular_valor_por_categoria():
    dados = carregar_dados()
    categorias = {}
    total_geral = 0
    
    for registro in dados:
        categoria = registro['categoria']
        valor = float(registro['valor'])
        total_geral += valor
        if categoria in categorias:
            categorias[categoria] += valor
        else:
            categorias[categoria] = valor
            
        if total_geral == 0:
            print("Nenhum registro encontrado.")
            return
            
        #lista ordenada
        categorias_ordenadas = sorted(
        	    categorias.items(),
        	    key=lambda item: item[1],
        	    reverse = True
        	)              
    
    for categoria, total in categorias_ordenadas: 
        porcentagem = (total / total_geral) * 100
        print("-----------------------------------------------------")
        print(f"Categoria: {categoria} \nValor total: R$ {total:.2f} \nPorcentagem {porcentagem:.2f}%")
    print("-----------------------------------------------------")

# Função para calcular o valor total por banco
def calcular_valor_por_banco():
    dados = carregar_dados()
    bancos = {}
    
    for registro in dados:
        banco = registro['banco']
        valor = float(registro['valor'])
        if banco in bancos:
            bancos[banco] += valor
        else:
            bancos[banco] = valor
    
    for banco, total in bancos.items():
        print("-----------------------------------------------------")
        print(f"Banco: {banco}, Valor total: R$ {total:.2f}")
    print("-----------------------------------------------------")


# Função para calcular o valor total por parcelamento
def calcular_valor_por_parcelamento():
    dados = carregar_dados()
    parcelamentos = {"À vista": 0, "Parcelado": 0}
    
    for registro in dados:
        valor = float(registro['valor'])
        if int(registro['total_parcelas']) == 1:
            parcelamentos["À vista"] += valor
        else:
            parcelamentos["Parcelado"] += valor
    
    for tipo, total in parcelamentos.items():
        print("-----------------------------------------------------")
        print(f"{tipo}: R$ {total:.2f}")
    print("-----------------------------------------------------")

def relatorio_parcelas_pendentes():
    dados = carregar_dados()
    pendentes = [registro for registro in dados if int(registro['parcela_atual']) < int(registro['total_parcelas'])]
    total_a_pagar_mes = sum(float(registro['valor']) for registro in pendentes)
    total_a_pagar = 0
    
    if not pendentes:
        print("Nenhuma parcela pendente encontrada.")
        return
    
    for registro in pendentes:
        parcelas_restantes = int(registro['total_parcelas']) - int(registro['parcela_atual'])

        print(f"\nData: {registro['data']}")
        print(f"Descrição: {registro['descricao']}")
        print(f"Parcela: {registro['parcela_atual']} de {registro['total_parcelas']}")
        print(f"Valor: R$ {float(registro['valor']):.2f}")
        print(f"Valor total restantes: {float(registro['valor']) * parcelas_restantes}")
        print(f"Categoria: {registro['categoria']}")
        print(f"Banco: {registro['banco']}")
        print("-----------------------------------------------------")
        total_a_pagar += float(registro['valor']) * parcelas_restantes
    print(f"Valor total a pagar no mes: R$ {total_a_pagar_mes:.2f}")
    print(f"Valor total de parcelas pendentes: R$ {total_a_pagar:.2f}")
    print("-----------------------------------------------------")

# Função para filtrar registros por intervalo de datas
def filtrar_por_intervalo_de_data():
    while True:
        data_inicio = input("Digite a data de início (DD-MM-YYYY): ")
        if validar_data(data_inicio):
            break
        print("Formato de data inválido! Use DD-MM-YYYY.")

    while True:
        data_fim = input("Digite a data de fim (DD-MM-YYYY): ")
        if validar_data(data_fim):
            break
        print("Formato de data inválido! Use DD-MM-YYYY.")

    data_inicio = datetime.strptime(data_inicio, '%d-%m-%Y')
    data_fim = datetime.strptime(data_fim, '%d-%m-%Y')

    dados = carregar_dados()
    filtrados = [
        registro for registro in dados 
        if data_inicio <= datetime.strptime(registro['data'], '%d-%m-%Y') <= data_fim
    ]

    if not filtrados:
        print("Nenhum registro encontrado nesse intervalo de datas.")
        return
   
    valor_total = 0
    dados_ordenados = sorted(filtrados, key=lambda x: datetime.strptime(x['data'], '%d-%m-%Y'))
    
    for registro in dados_ordenados:
        print(f"\nData: {registro['data']}")
        print(f"Descrição: {registro['descricao']}")
        print(f"Parcela: {registro['parcela_atual']} de {registro['total_parcelas']}")
        print(f"Valor: R$ {float(registro['valor']):.2f}")
        print(f"Categoria: {registro['categoria']}")
        valor_total += float(registro['valor'])
    #Formatar data
    data_inicio_str = data_inicio.strftime('%d-%m-%y')
    data_fim_str = data_fim.strftime('%d-%m-%y')    
    if data_inicio != data_fim:
        print(f"--------\nValor total dos gastos realizados entre {data_inicio_str} e {data_fim_str}: R${valor_total:.2f}\n----------")        
    else:
        print(f"--------\nValor total dos gastos realizados em {data_inicio_str}: R${valor_total:.2f}\n----------")        


# Menu principal
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Listar todos os registros")
        print("2. Adicionar novo registro")
        print("3. Alterar registro")
        print("4. Deletar registro")
        print("5. Filtrar registros por categoria")
        print("6. Filtrar registros por banco")
        print("7. Calcular valor total de todos os registros")
        print("8. Calcular valor total por categoria")
        print("9. Calcular valor total por banco")
        print("10. Calcular valor total por parcelamento")
        print("11. Relatorio de parcelas pendentes")
        print("12. Filtrar por data")
        print("13. Ordenar registros")
        print("14. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            listar_registros()
        elif opcao == '2':
            adicionar_registro()
        elif opcao == '3':
            alterar_registro()
        elif opcao == '4':
            deletar_registro()
        elif opcao == '5':
            filtrar_por_categoria()
        elif opcao == '6':
            filtrar_por_banco()
        elif opcao == '7':
            calcular_valor_total()
        elif opcao == '8':
            calcular_valor_por_categoria()
        elif opcao == '9':
            calcular_valor_por_banco()
        elif opcao == '10':
            calcular_valor_por_parcelamento()
        elif opcao == '11':
            relatorio_parcelas_pendentes()
        elif opcao == '12':
            filtrar_por_intervalo_de_data()    
        elif opcao == '13':
            ordenar_registros()
        elif opcao == '14':        
            print('Saindo')    
            break
        else:
            print("Opção inválida!")

# Executa o menu
if __name__ == "__main__":
    menu()