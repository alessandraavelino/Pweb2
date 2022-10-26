from helpers.database import db


class GestorApp(db.Model):

    __tablename__ = 'tb_gestorApp'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    
    def __init__(self, nome):
        self.nome = nome