from helpers.database import db


class Rota(db.Model):

    __tablename__ = 'tb_rota'

    id = db.Column(db.Integer, primary_key=True)
    cidadeDestino = db.Column(db.String(30), nullable=False)
    qtdAlunos = db.Column(db.String(3), nullable=False)
    prefeitura = db.Column(db.String(150), nullable=False)
    veiculo = db.Column(db.String(50), nullable=False)
    passageiros = db.Column(db.String(100), nullable=False)
    horaSaida = db.Column(db.Date(), nullable=False)
    horaChegada  = db.Column(db.Date(), nullable=False)
    def __init__(self, cidadeDestino, qtdAlunos, prefeitura, veiculo):
        self.cidadeDestino = cidadeDestino
        self.qtdAlunos = qtdAlunos
        self.prefeitura = prefeitura
        self.veiculo = veiculo

    def __repr__(self):
        return '<Rota %r>' % self.rota
