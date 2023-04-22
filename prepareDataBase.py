import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")

try:
    conn = mysql.connector.connect (
        host='127.0.0.1',
        user='root',
        password='admin'
    )
except mysql.connector.Error as err:
    if err.erno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuario ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `REGISTRO_ALUNOS_FAMERP`;")
cursor.execute("CREATE DATABASE `REGISTRO_ALUNOS_FAMERP`")
cursor.execute("USE `REGISTRO_ALUNOS_FAMERP`")

TABLES = {}
TABLES['USUARIOS'] = ('''
      CREATE TABLE `USUARIOS` (
      `ID` int(11) NOT NULL AUTO_INCREMENT,
      `NOME` varchar(100) NOT NULL,
      `EMAIL` varchar(100) UNIQUE NOT NULL,
      `SENHA` varchar(100) NOT NULL,
      PRIMARY KEY (`ID`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
    table_sql = TABLES[table_name]
    try:
        print('Generating table {}:'.format(table_name), end=' ')
        cursor.execute(table_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ABLE_EXISTS_ERROR:
            print('Already exists')
        else:
            print(err.msg)
    else:
        print('OK')

USUARIOS_sql = 'INSERT INTO USUARIOS (NOME, EMAIL, SENHA) VALUES (%s, %s, %s)'
USUARIOS = [
    ("Renan Augusto", "renan@teste.com.br", generate_password_hash("teste").decode('utf-8')),
    ("Usuario Teste", "teste@teste.com.br", generate_password_hash("teste").decode('utf-8'))
]
cursor.executemany(USUARIOS_sql, USUARIOS)
cursor.execute('select * from REGISTRO_ALUNOS_FAMERP.USUARIOS')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

conn.commit()

cursor.close()
conn.close()