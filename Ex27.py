def calcularVelMedia(extensaoCircuito, tempo, numVoltas):

    velMedia = (extensaoCircuito * numVoltas) / tempo
    return velMedia

def main():

    extensaoCircuito = int(input("Digite a extensão do circuito em metros: "))
    numVoltas = int(input("Digite o número de voltas: "))
    tempo = int(input("Digite o tempo de duração em minutos: "))
    print(calcularVelMedia(extensaoCircuito, tempo, numVoltas))


if __name__ == '__main__':
    main()