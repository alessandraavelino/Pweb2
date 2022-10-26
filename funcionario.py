from helpers.database import db


class Funcionario(db.Model):
    __tablename__ = "tb_funcionario"
    id = db.Column(db.Integer, primary_key=True)
    prefeitura = db.Column(db.String(50), nullable=False)
    cargo = db.Column(db.String(11), nullable=False)


    def __init__(self, id, prefeitura, cargo):
        self.id = id
        self.prefeitura = prefeitura
        self.cargo = cargo


    def __repr__(self):
        return '<Funcionario %r>' % self.funcionario
