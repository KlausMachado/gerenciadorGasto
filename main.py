from controleFinanceiro import listar_registros, adicionar_registro, alterar_registro, deletar_registro, filtrar_por_categoria, filtrar_por_banco, calcular_valor_total, calcular_valor_por_categoria, calcular_valor_por_banco, calcular_valor_por_parcelamento, relatorio_parcelas_pendentes, filtrar_por_intervalo_de_data, ordenar_registros
# Menu principal
def menu():
    print("Controle Financeiro - Versão 1.0")

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