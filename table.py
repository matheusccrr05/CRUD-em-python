import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gi02Ma05Nat08",
    database="bdcrud",
)

cursor = conexao.cursor()

#create 
nome_produto = "sopa"
valor = 7
comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()

# #read
comando = "SELECT * FROM vendas"
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

# #update
nome_produto = "macarrão"
valor = 10
comando = f'UPDATE vendas SET nome_produto = "{nome_produto}"WHERE valor = {valor}'
cursor.execute(comando)
conexao.commit()

#delete
nome_produto = "uva"
comando = f'DELETE FROM vendas WHERE idVendas = 20'
cursor.execute(comando)
conexao.commit()

conexao.close()
cursor.close()