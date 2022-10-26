from helpers.database import db


class Aluno(db.Model):

    __tablename__ = 'tb_aluno'
    id = db.Column(db.Integer, primary_key=True)
    instituicaoEnsino = db.Column(db.String(50), nullable=False)
    curso = db.Column(db.String(30), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    def __init__(self, id, nome, curso, matricula):
        self.id = id
        self.nome = nome
        self.curso = curso
        self.matricula = matricula

    def __repr__(self):
        return '<Aluno %r>' % self.aluno
