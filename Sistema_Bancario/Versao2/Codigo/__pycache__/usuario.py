usuarios = []
detalhes_usuarios = {}

def criar_usuario():
    print("Criar Usuário")

    nome = str(input("Digite seu nome completo: "))
    nasc = str(input("Digite sua data de nascimento (XX/XX/XXXX): "))
    cpf = str(input("Digite seu CPF (apenas números): "))

    logradouro = str(input("Logradouro: "))
    nmr = int(input("Número da casa: "))
    bairro = str(input("Bairro: "))
    cidade = str(input("Cidade: "))
    estado = str(input("Estado: "))

    endereco = {
        "logradouro": logradouro,
        "numero": nmr,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado
    }

    dici = {
        "nome": nome,
        "nascimento": nasc,
        "CPF": cpf,
        "endereço": endereco
    }

    usuarios.append(nome)
    detalhes_usuarios[nome] = dici

    print("Usuário criado com sucesso!")
    print("Lista de usuários:")
    for i, user in enumerate(usuarios, 1):
        print(f"{i}. {user}")

def consultar_usuario():
    nome = str(input("Digite o nome do usuário que deseja consultar: "))
    if nome in detalhes_usuarios:
        user = detalhes_usuarios[nome]
        print(f"Nome: {user['nome']}")
        print(f"Nascimento: {user['nascimento']}")
        print(f"CPF: {user['CPF']}")
        print("Endereço:")
        endereco = user['endereço']
        print(f"  Logradouro: {endereco['logradouro']}")
        print(f"  Número: {endereco['numero']}")
        print(f"  Bairro: {endereco['bairro']}")
        print(f"  Cidade: {endereco['cidade']}")
        print(f"  Estado: {endereco['estado']}")
    else:
        print("Usuário não encontrado.")

criar_usuario()
consultar_usuario()