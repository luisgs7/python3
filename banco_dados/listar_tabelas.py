import enum
from os import curdir
from db import nova_conexao

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute('SHOW TABLES;')

    for i, table in enumerate(cursor, start=1):
        print(f'Tabela {i}: {table[0]}')