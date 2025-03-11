def menu():
    print("BEM VINDO AO CAIXA ELETRONICO")
    print("O QUE VOCE DESEJA FAZER:")
    print(" S - SAQUE")
    print(" D - DEPOSITAR")
    print(" E - EXTRATO")
    print(" NC - CRIAR NOVA CONTA")
    print(" NU - CRIAR NOVO USARIO")
    print(" Q - SAIR")
    escolha = input("ESCOLHA UMA OPÇÃO: ")
    escolha = escolha.upper()
    return escolha

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        return print("VALOR INVALIDO")
    elif valor > limite:
        return print("VALOR MAIOR QUE O LIMITE DE SAQUE")
    elif numero_saques > limite_saques:
        return print("NUMERO DE SAQUES EXCEDIDO")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        return print("OPERACAO INVALIDA")
    
def deposito(saldo, valor, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato = f"Depósito: R$ {valor:.2f}\n"
        return extrato
    else:
        return print("Operação falhou! O valor informado é inválido.")


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    for valor in usuarios:
        if valor == cpf:
            usuario = usuario + 1

    if usuario == 1:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado! ")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    for usuario in usuarios:
        if usuario == cpf :
            print("\nJá existe usuário com esse CPF! ")
            return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_contas = 0

    while True:
        if menu() == 'Q':
            print("Obrigado por usar o caixa eletronico")
            break

        elif menu() == 'S':
            valor = float(input("QUAL O VALOR VOCE DEJEJA SACAR?"))
            saque(saldo = saldo, valor = valor, limite=limite, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES)
        
        elif menu() == 'D':
            deposito(saldo, valor, extrato)
        
        elif menu() == 'NC':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif menu() == 'NU':
            numero_contas += 1 
            criar_usuario(AGENCIA, numero_contas, usuarios)
        elif menu() == 'E':
            extrato(saldo, extrato=extrato)
        
        else:
            print("OPÇÃO INVALIDA")

if __name__ == '__main__':
    main()