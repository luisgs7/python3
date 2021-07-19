lista = [1, 2, 3, 'oi', 'ola']

a = 3
b = a
c = 3

print(a is b)
print(a is not c)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_a is lista_c)
print(lista_a is not lista_c)
