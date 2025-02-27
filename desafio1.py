menu = """
======BANTUN======
[1] DEPOSITO
[2] SAQUE
[3] EXTRATO
[0] SAIR
==================
"""
saldo, num_saque = 0, 0
limite = 500
extrato = ""
limite_saque = 3


while True:
    option = int(input(menu))
    if option == 1:
        value = float(input("Informe o valor do deposito: "))
        if value > 0:
            saldo += value
            extrato += f"Deposito: R${value:.2f}\n"
            print(f"\033[35mVocê depositou R${value} reais\033[0m")
        else:
            print("\033[31mFalha na Operação, por favor Revise o valor informado\033[0m")
    elif option == 2:
        value = float(input("Informe o valor do saque R$ "))
        excedeu_saldo = value > saldo
        excedeu_limite = value > limite
        excedeu_saque = num_saque >= limite_saque
        if excedeu_saldo:
            print("\033[33mAtenção, Saldo Insuficiente\033[0m")
        elif excedeu_limite:
            print("\033[33mAtenção, Limite Excedido\033[0m")
        elif excedeu_saque:
            print("\033[33mAtenção, Limites de Saque Excedido\033[0m")
        elif value > 0:
            saldo -= value
            extrato += f"Saque: R${value:.2f}\n"
            num_saque += 1
            print(f"\033[35mVocê Sacou R${value} reais\033[0m")
        else:
            print("\033[31mOperação Invalida, informe um novo valor\033[0m")

    elif option == 3:
        texto = "EXTRATO"
        print(f"{'='*5}{texto}{'='*5}")
        print(f"Não foram realizadas Movimentações" if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("="*17)

    elif option == 0:
        print("\033[36m Obrigado por usar os serviços do BANTUN, até a próxima\033[0m")
        break
    else:
        print("\033[31mOperação Invalida, digite a opção desejada\033[0m")
