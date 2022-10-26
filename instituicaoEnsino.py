from helpers.database import db


class InstituicaoEnsino(db.Model):
    __tablename__ = "tb_instituicaoEnsino"

    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(20), nullable=False)

    def __init__(self, id, endereco, telefone, nome):
        self.id = id
        self.endereco = endereco
        self.telefone = telefone
        self.nome = nome

    def __repr__(self):
        return '<InstituicaoEnsino %r>' % self.instituicaoEnsino
