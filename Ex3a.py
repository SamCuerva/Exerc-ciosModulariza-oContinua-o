def fat(n):

    fat: int = 1
    for i in range(1, n + 1):
        
        fat *= i 

    return fat

def main():

    num = int(input("Digite um valor: "))
    res = fat(num)
    print(res)

if __name__ == '__main__':
    main()