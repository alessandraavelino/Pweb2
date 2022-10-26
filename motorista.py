from helpers.database import db


class Motorista(db.Model):
    __tablename__ = "tb_motorista"

    rotas = db.Column(db.String(100), nullable=False)



    def __init__(self, rotas):
        self.rotas = rotas


    def __repr__(self):
        return '<Motorista %r>' % self.motorista
