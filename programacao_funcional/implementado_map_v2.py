def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == "__main__":
    resultado = mapear(lambda a: a ** 2, [2, 3, 4])
    print(list(resultado))
