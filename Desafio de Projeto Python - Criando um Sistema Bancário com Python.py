# Desafio de Projeto Python - Criando um Sistema Bancário com Python
# Criar um Sistema bancário com as operações: sacar, depositar e visualizar extrato.

menu= """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo= 0
limite= 500
extrato= []
numero_saques= 0
limite_saques= 3
numero_depositos= 0

while True:
    opcao= input(menu)

    if opcao == "d":
        print("Depósito")
        deposito= float(input("Quanto você quer Depositar: "))
        
        while deposito <0:
            print("O Depósito não pode ser negativo, tente novamente")
            deposito= float(input("Quanto você quer Depositar: "))
            if deposito >=0:
                break
            else:
                continue
        saldo += deposito
        numero_depositos += 1
        extrato.append(f'Feito 1 depósito no valor de R${deposito}')
        print("Depósito Realizado com Sucesso.")


    elif opcao == "s":
        print("Sacar")
        if limite_saques == 0:
            print("Você atingiu o limite máximo de saques por hoje.")
        else:
            sacar= float(input("Quanto você quer sacar: "))
            if saldo < sacar:
                print("Saldo insuficiente. Tente outro valor.")
            else:
                if sacar > 0 and sacar < 500:
                    print("Saque feito.")
                    saldo -= sacar
                    limite_saques -= 1
                    extrato.append(f'Feito 1 saque no valor de R${sacar}')
                    print("Saldo Realizado com Sucesso.")
                else:
                    print("O valor máximo para saque é de R$500,00. E o mínimo é R$1,00. Não pode ultrapssar isso.")
                    print("Tente novamente")

    elif opcao == "e":
        print("Extrato")
        for numero in extrato:
            print(numero)
        print(f'Saldo atual: R${saldo}')
        print("Extrato realizado com Sucesso.")

    elif opcao == "q":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")