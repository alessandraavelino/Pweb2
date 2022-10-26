from helpers.database import db


class Uf(db.Model):
    __tablename__ = "tb_uf"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(11), nullable=False)
    sigla = db.Column(db.String(11), nullable=False)


    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla


    def __repr__(self):
        return '<Uf %r>' % self.uf
