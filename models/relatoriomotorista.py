from configMotorista import db


class Relatorio(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeApp = db.Column(db.String(255))
    Mensagem = db.Column(db.String(255))
    nome_relatorio = db.Column(db.String(255))
    tipo_plataforma = db.Column(db.String(255))
    status = db.Column(db.String(255))
    dataHora = db.Column(db.String(255))
    
    
    def __init__(self, nomeApp, Mensagem,nome_relatorio,tipo_plataforma,status, dataHora):
        self.nomeApp = nomeApp
        self.Mensagem = Mensagem
        self.nome_relatorio = nome_relatorio
        self.tipo_plataforma = tipo_plataforma
        self.status= status
        self.dataHora = dataHora