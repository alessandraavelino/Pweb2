from helpers.database import db


class Cidade(db.Model):
    __tablename__ = "tb_cidade"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(11), nullable=False)
    sigla = db.Column(db.String(11), nullable=False)


    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla


    def __repr__(self):
        return '<Cidade %r>' % self.cidade
