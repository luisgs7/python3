from os import curdir
from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s);'
args = (
    ('Ana', '98765-4321'),
    ('Bia', '98965-4321'),
    ('Luca', '99765-4321'),
    ('Lu', '98565-4321'),
    ('Luis', '98705-4321'),
    ('Beca', '98768-4321'),
    ('José', '98065-4321'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()

    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

    else:
        print(f'Foram incluídos {cursor.rowcount}registros!')
