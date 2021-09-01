#! /usr/bin/python

# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci():
    penultimo = 0
    ultimo = 1
    i = 0
    print(f'{penultimo},{ultimo}', end=',')

    while i < 1000:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo

        i += 1


if __name__ == '__main__':
    fibonacci()
