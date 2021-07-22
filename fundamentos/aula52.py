tupla = tuple()
tupla = ()

print(type(tupla))

# dir(tupla)
# help(tupla)

tupla = ('um',)  # tupla de somente 1 elemento adicionar virgula no final
print(type(tupla))

print(tupla[0])

cores = ('verde', 'amarelo', 'azul', 'branco')

print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.index('azul'))

print(len(cores))
