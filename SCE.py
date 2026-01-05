# Escolha = int(input("Escolha uma opção entre (1, 2 e 3): "))

# match Escolha:
#     case 1:
#         print("Você escolheu a opção 1")
# Mensagem de inicio
Mensagem_de_inicio = "====== Olá, seja bem vindo ====== "
Mensagem_de_inicio_2 = "Por Favor, selecione a opção que deseja realizar aqui no nosso site"

print(Mensagem_de_inicio)
print(Mensagem_de_inicio_2)

# Criando as listas de produtos
produtos = ["Arroz", "Carne", "Maçã", "tomate"]
preço_dos_produtos = {"Arroz": 10, "Carne": 20, "Maçã": 5, "tomate": 3}

# Criando as opções
opções = int(input("1 - Ver o estoque, 2 - Comprar produtos, 3 - Sair: "))

match opções:
    case 1:
        print("Produtos disponíveis:")
        for produto in produtos:
            print(f"{produto}: R${preço_dos_produtos[produto]}")
    case 2:
        produto_1 = input(f'Digite o primeiro produto {produtos}: ').capitalize()
        produto_2 = input(f'Digite o segundo produto {produtos}: ').capitalize()

        # Verifica se os produtos existem no estoque
        if produto_1 in preço_dos_produtos and produto_2 in preço_dos_produtos:
            total = preço_dos_produtos[produto_1] + preço_dos_produtos[produto_2]
            print(f"Total da compra: R${total}")
        else:
            print("Um ou ambos os produtos digitados não estão disponíveis.")
    case 3:
        print("Obrigado, volte sempre!")
    case _:
        print("Opção inválida!")
   
        