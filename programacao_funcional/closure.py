def multiplicar(a):
    def calcular(b):
        return a * b
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)

    print(dobro)
    print(triplo)

    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')
