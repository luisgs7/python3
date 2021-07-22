from string import Template

nome, idade = 'pedro', 30

print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {0} Idade: {1}'.format(nome, idade))  # python < 3.6
print(f'Nome: {nome} Idade: {idade}')  # python >= 3.6

s = Template('Nome: $nome Idade $idade')

print(s.substitute(nome=nome, idade=idade))
