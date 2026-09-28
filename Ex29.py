def calcularInvestimento(tipoInvestimento, valorInvestimento):

    if tipoInvestimento == 1:

        valorCorrigido = valorInvestimento * 1.03

    elif tipoInvestimento == 2:

        valorCorrigido = valorInvestimento * 1.05

    return valorCorrigido

def main():

    tipoInvestimento = int(input("Digite o tipo de investimento(1 - poupança 2 - renda fixa): "))
    valorInvestimento = float(input("Digite o valor: "))
    print(calcularInvestimento(tipoInvestimento, valorInvestimento))


if __name__ == '__main__':
    main()