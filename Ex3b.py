def div(n1, n2):
    return n1 / n2


def fat(n):
    fatorial: int = 1

    for i in range(1, n + 1):
        fatorial *= i

    return fatorial


def main():
    num1 = int(input("Digite um valor: "))
    soma = 1

    for i in range(1, num1 + 1):
        resultado_fat = fat(i)
        soma += div(1, resultado_fat)

    print(soma)


if __name__ == '__main__':
    main()
