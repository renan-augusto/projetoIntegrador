from spe import db
from werkzeug.security import generate_password_hash, check_password_hash

class ALUNO(db.Model):
    __tablename__ = "ALUNO"
    IDALUNO = db.Column(db.Integer, primary_key = True, autoincrement = True)
    NOME = db.Column(db.String(100), nullable = False)
    EMAIL = db.Column(db.String(50), unique = True, nullable = False)
    RA = db.Column(db.String(8), unique = True, nullable = False)
    SENHA = db.Column(db.String(128), nullable = False)
    def __repr__(self) :
        return '<Name %r>' % self.name 
    def __init__(self, NOME, EMAIL, RA, SENHA):
        self.NOME = NOME 
        self.EMAIL = EMAIL
        self.RA = RA
        self.SENHA = generate_password_hash(SENHA)
        
    def verify_password(self, pwd):
        return check_password_hash(self.SENHA, pwd)
    
    
#class PROFESSOR(db.Model):
#    __tablename__ = "PROFESSOR"   
#    IDPROFESSOR = db.Column(db.Integer, primary_key = True, autoincrement = True),
#    NOME = db.Column(db.String(100), nullable = False),
#    EMAIL = db.Column(db.String(50), unique = True, nullable = False)
#    SENHA = db.Column(db.String(128), nullable = False)
#    def __repr__(self):
#        return '<Name % r>' % self.name
#    
#    def __init__(self, NOME, EMAIL, SENHA):
#        self.NOME = NOME
#        self.EMAIL = EMAIL
#        self.SENHA = generate_password_hash(SENHA)
#        
#    def verify_password(self, pwd):
#        return check_password_hash(self.SENHA, pwd)
    
