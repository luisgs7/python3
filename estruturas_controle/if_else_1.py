#!/usr/local/bin/python


def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota inválida'

    elif nota > 8:
        return 'A'

    elif nota > 5:
        return 'Recuperação'

    elif nota >= 0:
        return 'Reprovado'

    else:
        return 'Nota inválida'


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
