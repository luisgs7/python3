from mysql.connector import connect

conexao = connect(
    host="172.17.0.2",
    port=3306,
    user="root",
    passwd=""
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES;')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')
