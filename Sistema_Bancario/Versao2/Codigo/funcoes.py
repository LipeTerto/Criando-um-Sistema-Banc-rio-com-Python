usuarios = []
detalhes_usuarios = {}
contas = []
detalhes_conta = {}

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
    detalhes_usuarios[cpf] = dici

    print("Usuário criado com sucesso!")
    print("Lista de usuários:")
    for i, user in enumerate(usuarios, 1):
        print(f"{i}. {user}")

def criar_conta():
    print("Criar Conta Corrente")
    nome = str(input("Digite o nome completo do Usuário: "))
    cpf = str(input("Digite o CPF do Usuário: "))

    if cpf in detalhes_usuarios and detalhes_usuarios[cpf]['nome'] == nome:
        print("Criação da Conta Corrente")
        email = str(input("Digite um email: "))
        senha = str(input("Digite uma senha: "))
        agencia = "0001"

        conta_corrente = {
            "usuario": nome,
            "cpf": cpf,
            "email": email,
            "senha": senha,
            "agencia": agencia,
            "saldo": 0,
            "extrato": [],
            "limite_saques": 3
        }

        contas.append(conta_corrente)
        detalhes_conta[email] = conta_corrente

        print("Conta Corrente criada com sucesso!")
        print("Detalhes da Conta Corrente:")
        print(f"Titular: {nome}")
        print(f"Agência: {agencia}")
        print(f"Número da Conta: {len(contas)}")  # Usando o índice como número da conta
    else:
        print("Usuário não encontrado ou CPF incorreto. Por favor, tente novamente.")

def deposito():
    email = str(input("Digite o email da conta: "))
    if email in detalhes_conta:
        valor = float(input("Digite o valor a ser depositado: "))
        detalhes_conta[email]["saldo"] += valor
        detalhes_conta[email]["extrato"].append(f"Depósito: +{valor}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def saque():
    email = str(input("Digite o email da conta: "))
    if email in detalhes_conta:
        valor = float(input("Digite o valor a ser sacado: "))
        conta = detalhes_conta[email]
        if conta["saldo"] >= valor and valor <= 500 and conta["limite_saques"] > 0:
            conta["saldo"] -= valor
            conta["extrato"].append(f"Saque: -{valor}")
            conta["limite_saques"] -= 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente, valor maior que R$500 ou limite de saques atingido.")
    else:
        print("Conta não encontrada.")

def fun_extrato():
    email = str(input("Digite o email da conta: "))
    if email in detalhes_conta:
        conta = detalhes_conta[email]
        print("Extrato da conta:")
        for item in conta["extrato"]:
            print(item)
        print(f"Saldo atual: R${conta['saldo']:.2f}")
    else:
        print("Conta não encontrada.")
