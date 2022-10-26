from helpers.database import db


class Passageiro(db.Model):

    __tablename__ = 'tb_passageiro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    cidadeOrigem = db.Column(db.String(30), nullable=False)
    cidadeDestino = db.Column(db.String(30), nullable=False)

    def __init__(self, id, nome, cidadeOrigem, cidadeDestino):
        self.id = id
        self.nome = nome
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return '<Passageiro %r>' % self.passageiro
