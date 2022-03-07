from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json 

app = Flask(__name__)                   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/FlaskDB'
                                    #Banco://Usuario:senha@porta:YYYY/NomeDoBanco
db=SQLAlchemy(app)

class teste_aplicativo(db.Model):
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

def envia_dados(nomeApp, Mensagem,nome_relatorio,tipo_plataforma,status, dataHora):
    nomeApp = json.dumps(nomeApp)
    Mensagem = json.dumps(Mensagem)
    nome_relatorio = json.dumps(nome_relatorio)
    tipo_plataforma = json.dumps(tipo_plataforma)
    status = json.dumps(status)
    dataHora = json.dumps(dataHora)
    
    try:
        relatorio = teste_aplicativo(nomeApp=nomeApp, 
        Mensagem = Mensagem,
        nome_relatorio=nome_relatorio,
        tipo_plataforma=tipo_plataforma,
        dataHora=dataHora,
        status=status)
        db.session.add(relatorio)
        db.session.commit()
        return Response()
        
    except Exception as erro:
        print(erro)
        return False




if __name__ == '__main__':
    app.config['SECRET_KEY'] = "159753"
    db.init_app(app)
    app.run(debug = True)