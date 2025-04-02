# Gerenciador Financeiro - Aplicação em Python

Um aplicativo simples para gerenciar finanças pessoais e controlar gastos, receitas e transações financeiras.

## 📌 Funcionalidades

- **Operações CRUD**: Criar, Ler, Atualizar e Excluir registros financeiros
- **Filtros**: Filtrar transações por categoria, banco ou período
- **Relatórios**: Gerar diversos resumos e cálculos financeiros
- **Armazenamento em CSV**: Todos os dados são salvos em arquivo CSV

## 🐍 Conceitos de Python Demonstrados

Este projeto utiliza vários conceitos importantes de programação Python:

### Manipulação de Arquivos
- Leitura e escrita de arquivos CSV com o módulo `csv`
- Verificação de existência de arquivos com `os.path`
- Persistência de dados entre sessões

### Estruturas de Dados
- Listas e dicionários para armazenar transações
- Operações com conjuntos (sets) para categorias/bancos únicos
- Ordenação com funções personalizadas usando `lambda`

### Trabalhando com Datas
- Validação de datas com `datetime.strptime`
- Comparação e ordenação de datas
- Formatação de datas para exibição

### Programação Funcional
- List comprehensions para filtrar dados
- Funções lambda para ordenação
- Operações com dicionários para agregação de dados

### Tratamento de Erros
- Validação de entradas do usuário
- Blocos try-except para maior robustez

### Organização de Código
- Funções modulares para cada funcionalidade
- Separação clara de responsabilidades
- Interface baseada em menu

## 🚀 Como Usar

1. Execute o script em um ambiente Python
2. Use o menu para:
   - Adicionar novas transações (com data, descrição, valor, etc.)
   - Visualizar/editar registros existentes
   - Gerar relatórios financeiros
   - Filtrar transações por diversos critérios

## 📊 Relatórios Disponíveis

- Total de gastos por categoria (com porcentagens)
- Resumo de despesas por banco
- Relatório de parcelas pendentes
- Transações filtradas por período

## 📝 Requisitos

- Python 3.x
- Nenhuma dependência externa necessária

Este projeto serve como uma aplicação prática dos conceitos fundamentais de Python enquanto oferece funcionalidades úteis para controle financeiro pessoal.
