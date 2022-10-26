from helpers.database import db


class Endereco(db.Model):
    __tablename__ = "tb_endereco"

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(11), nullable=False)
    numero = db.Column(db.String(11), nullable=False)
    complemento = db.Column(db.String(20), nullable=False)
    referencia = db.Column(db.String(50), nullable=False)
    logradouro = db.Column(db.String(80), nullable=False)

    def __init__(self, id, cep, numero, complemento, referencia, logradouro):
        self.id = id
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.referencia = referencia
        self.logradouro = logradouro

    def __repr__(self):
        return '<Endereco %r>' % self.endereco
