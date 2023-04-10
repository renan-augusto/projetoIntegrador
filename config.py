SECRET_KEY = 'grupo1sjrp'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost', 
        database = 'REGISTRO_ALUNOS_FAMERP'
    )