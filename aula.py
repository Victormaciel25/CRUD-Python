import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdyoutube',
)

cursor = conexao.cursor()

# CRUD
nome_produto = 'todynho'
valor = 3
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ({nome}, {valor})'
cursor.execute(comando) # manda o comando ser executado
conexao.commit() # edita o banco de dados
# resultado = cursor.fetchall() # ler o banco de dados

cursor.close()
conexao.close()