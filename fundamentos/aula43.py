# print(dir(int))
# print(dir(float))

a = 5
b = 2.5
a / b
a + b
a * b

type(a)
type(b)
type(a - b)

print(b.is_integer())
print(5.0.is_integer())
print(6.1.is_integer())

soma = int.__add__(2, 3)
print(soma)

print((-2).__abs__())

print((-3.6).__abs__())
