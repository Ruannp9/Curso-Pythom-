#crie um programa que exiba um menu interativo com as seguintes opções:
#1-adicionar item
#2 - remover item
#3- exibir lista
# 4- sair




lista_de_compras = []


def adicionar_item(item):
    lista_de_compras.append(item)
    print(f"'{item}' foi adicionado à lista de compras.")


def remover_item(index):
    try:
        item_removido = lista_de_compras.pop(index)
        print(f"'{item_removido}' foi removido da lista de compras.")
    except IndexError:
        print("Índice inválido. Por favor, insira um índice válido.")


def listar_itens():
    if len(lista_de_compras) > 0:
        print("\nLista de Compras:")
        for index, item in enumerate(lista_de_compras):
            print(f"{index} - {item}")
    else:
        print("A lista de compras está vazia.")


def main():
    while True:
        print("\n--- Lista de Compras ---")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Listar Itens")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            item = input("Digite o nome do item a ser adicionado: ")
            adicionar_item(item)
        elif opcao == '2':
            listar_itens()
            if len(lista_de_compras) > 0:
                index = int(input("Digite o índice do item a ser removido: "))
                remover_item(index)
        elif opcao == '3':
            listar_itens()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()