from db import nova_conexao

sql = 'SELECT * FROM contatos WHERE tel = "98765-4321";'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for a in cursor:
        print(a)