from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json 

<<<<<<< HEAD:setup.py
app = Flask(__name__)                   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/FlaskDB'
                                    #Banco://Usuario:senha@porta:YYYY/NomeDoBanco
db=SQLAlchemy(app)
=======
app = Flask(__name__)                   #Banco://Usuario:senha@porta:YYYY/NomeDoBanco
db = app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/dbtest1'
>>>>>>> 879042835c3e53bcf2cb4f69d6592012a2af6fb4:models/setup.py

class teste_aplicativo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeApp = db.Column(db.String(255))
    Mensagem = db.Column(db.String(255))
    nome_relatorio = db.Column(db.String(255))
    tipo_plataforma = db.Column(db.String(255))
    status = db.Column(db.String(255))
    
    
    def __init__(self, nomeApp, Mensagem,nome_relatorio,tipo_plataforma,status):
        self.nomeApp = nomeApp
        self.Mensagem = Mensagem
        self.nome_relatorio = nome_relatorio
        self.tipo_plataforma = tipo_plataforma
        self.status= status

def envia_dados(nomeApp, Mensagem,nome_relatorio,tipo_plataforma,status):
    nomeApp = json.dumps(nomeApp)
    Mensagem = json.dumps(Mensagem)
    nome_relatorio = json.dumps(nome_relatorio)
    tipo_plataforma = json.dumps(tipo_plataforma)
    status = json.dumps(status)
    
    try:
        relatorio = teste_aplicativo(nomeApp=nomeApp, 
        Mensagem = Mensagem,
        nome_relatorio=nome_relatorio,
        tipo_plataforma=tipo_plataforma,
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