def calcularPrecoNovo(precoAtual, mediaMensal):

    aumentoDoPreco: float = 0
    precoNovo: float = 0

    if mediaMensal < 500 and precoAtual < 30:

        aumentoDoPreco = 1.10

    elif mediaMensal >= 500 and mediaMensal < 1000 and precoAtual >= 30 and precoAtual < 80:
        
        aumentoDoPreco = 1.15

    elif mediaMensal >= 1000 and precoAtual >= 80:
        
        aumentoDoPreco = 0.95

    else:

        aumentoDoPreco = 1.00

    precoNovo = precoAtual * aumentoDoPreco

    return precoNovo


def main():

    precoAtual  = float(input("Digite o preço atual: "))
    mediaMensal = float(input("Digite a média mensal: "))
    print(calcularPrecoNovo(precoAtual, mediaMensal))

if __name__ == '__main__':
    main()