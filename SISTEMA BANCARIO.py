##SISTEMA BANCARIO

print(""" SISTEMA BANCARIO 
          MENU PRINCIPAL
    D - Deposito(VALORES POSTIVOS)
    S - SAQUE(VALORES POSTIVOS)
    V - VISUALIZAR ESTRATO
    E - SAIR
""")


conta_valor = 10000
contagem_saque = 0
opcao = input("DIGITE UMA OPÇÃO: ").upper()
while True:
    if opcao == "D":
        valor = float(input("DIGITE O VALOR DO DEPOSITO: "))

        if valor > 0:
            conta_valor += valor
            print(f"VALOR DE DEPOSITADO R${valor:.2f}")
        else:
            print("VALOR INVALIDO")

    elif opcao == "S":
        valor = float(input("DIGITE O VALOR DO SAQUE: "))
        if contagem_saque > 2:
            print("VOCE JÁ FEZ 3 SAQUES, FUNCAO INDISPONIVEL")

        elif valor > 0 and conta_valor >= valor:
            conta_valor -= valor
            print(f"VALOR DE SAQUE R${valor:.2f}")
            contagem_saque += 1

        else:
            print("VALOR INVALIDO")

    elif opcao == "V":
        print(f"SEU EXTRATO É DE R${conta_valor:.2f}")

    elif opcao == "E":
        print("OBRIGADO POR USAR O SISTEMA BANCARIO")
        break

    else:
        print("OPÇÃO INVALIDA, TENTE NOVAMENTE")


    opcao = input("OQ DESEJA FAZER AGORA?").upper()
