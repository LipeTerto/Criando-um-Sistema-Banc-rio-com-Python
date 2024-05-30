from funcoes import *

menu1= """
 [c] Criar Usuário
 [e] Entrar
 [q] Sair
=> """

menu2= """
[c] Criar Conta Corrente
[e] Entrar em uma Conta Corrente
[q] Sair
=> """

menu3= """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

while True:
    opcao1 = input(menu1).lower()

    if opcao1 == "c":
        criar_usuario()
    elif opcao1 == "e":
        nome = str(input("Digite o nome completo do Usuário: "))
        cpf = str(input("Digite o CPF do Usuário: "))
        
        if cpf in detalhes_usuarios and detalhes_usuarios[cpf]['nome'] == nome:
            while True:
                opcao2 = input(menu2).lower()

                if opcao2 == "c":
                    criar_conta()
                elif opcao2 == "e":
                    email = str(input("Digite o email: "))
                    senha = str(input("Digite a senha: "))

                    if email in detalhes_conta and detalhes_conta[email]['senha'] == senha:
                        while True:
                            opcao3 = input(menu3).lower()
                            if opcao3 == "d":
                                deposito()
                            elif opcao3 == "s":
                                saque()
                            elif opcao3 == "e":
                                fun_extrato()
                            elif opcao3 == "q":
                                break
                            else:
                                print("Operação Inválida, por favor selecione novamente a operação desejada.")
                    else:
                        print("Email ou Senha incorretos. Tente Novamente")
                elif opcao2 == "q":
                    break
                else:
                    print("Operação Inválida, por favor selecione novamente a operação desejada.")
        else:
            print("Usuário ou CPF incorretos. Tente Novamente")
    elif opcao1 == "q":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
