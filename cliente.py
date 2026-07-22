clientes = []


def cadastrar_cliente():
    print("\n=== Cadastro de Cliente ===")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    clientes.append(cliente)

    print("\n✅ Cliente cadastrado com sucesso!")
