from helpers.database import db


class Veiculo(db.Model):
    __tablename__ = "tb_veiculo"

    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(11), nullable=False)
    qtdPassageiros = db.Column(db.String(4), nullable=False)
    tipoVeiculo = db.Column(db.String(11), nullable=False)
    placa = db.Column(db.String(7), nullable=False)


    def __init__(self, id, cidade, qtdPassageiros, tipoVeiculo, placa):
        self.id = id
        self.cidade = cidade
        self.qtdPassageiros = qtdPassageiros
        self.tipoVeiculo = tipoVeiculo
        self.placa = placa


    def __repr__(self):
        return '<Veiculo %r>' % self.veiculo
