from mysql.connector import connect

conexao = connect(
    host="172.17.0.2",
    port=3306,
    user="root",
    passwd=""
)

cursor = conexao.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS agenda;')
