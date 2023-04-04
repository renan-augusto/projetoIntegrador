from spe import db

class ALUNO(db.Model):
    IDALUNO = db.Column(db.Integer, primary_key = True, autoincrement = True)
    NOME = db.Column(db.String(100), nullable = False)
    CPF = db.Column(db.String(11), unique = True )
    DATANASCIMENTO = db.Column(db.String(10), nullable = False) #confirmar
    SEXO = db.Column(db.String(1), nullable = False), #confirmar
    EMAIL = db.Column(db.String(50), unique = True)
    SEMESTRE = db.Column(db.String(1), nullable = False), 
    RA = db.Column(db.String(8), unique = True, nullable = False)
    def __repr__(self) :
        return '<Name %r>' % self.name 

class PROFESSOR(db.Model):
    IDPROFESSOR = db.Column(db.Integer, primary_key = True, autoincrement = True),
    NOME = db.Column(db.String(100), nullable = False),
    SEXO = db.Column(db.String(1), nullable = False), #confirmar
    CPF = db.Column(db.String(11), nullable = False)
    def __repr__(self):
        return '<Name % r>' % self.name