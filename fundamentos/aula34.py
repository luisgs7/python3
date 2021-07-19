print(True and True)
print(False and True)

print(False or True)
print(False or False)

print(True != True)
print(False != True)
print(False != False)

print(not True)
print(not False)

print(not 1)
print(not not 1)

saldo = 1000
salario = 4000
despesas = 3900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas

print(meta)
