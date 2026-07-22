from cliente import cadastrar_cliente
from database import criar_tabela


def exibir_menu():
    print("\n" + "=" * 40)
    print(" SISTEMA DE CADASTRO DE CLIENTES")
    print("=" * 40)
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Buscar Cliente")
    print("4 - Atualizar Cliente")
    print("5 - Excluir Cliente")
    print("6 - Sair")
    print("=" * 40)


def main():

    criar_tabela()

    while True:

        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            print("\n🚧 Função será implementada em breve.")

        elif opcao == "3":
            print("\n🚧 Função será implementada em breve.")

        elif opcao == "4":
            print("\n🚧 Função será implementada em breve.")

        elif opcao == "5":
            print("\n🚧 Função será implementada em breve.")

        elif opcao == "6":
            print("\nSistema encerrado. Até logo!")
            break

        else:
            print("\n❌ Opção inválida!")


if __name__ == "__main__":
    main()