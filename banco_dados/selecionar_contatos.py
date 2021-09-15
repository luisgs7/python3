from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s;'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (10, 10))
        contatos = cursor.fetchall()

    except:
        print(f'Erro: {e.msg}')

    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} Telefone {contato[1]}')
