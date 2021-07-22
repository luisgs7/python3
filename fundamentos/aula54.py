pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}

pessoa['idade'] = 44
pessoa['cursos'].append('Angular')

print(pessoa)

pessoa.pop('idade')

print(pessoa)

pessoa.update({'idade': 50, 'estado': 'tocantins'})

print(pessoa)

pessoa.clear()

print(pessoa)
