from flask import Response
from models.relatoriomotorista import Relatorio
from configMotorista import db
import mysql.connector
import json 

class Gerando_Relatorio():

    def gerando_relatorio(nomeApp, Mensagem,nome_relatorio,tipo_plataforma,status, dataHora):
        nomeApp = json.dumps(nomeApp)
        Mensagem = json.dumps(Mensagem)
        nome_relatorio = json.dumps(nome_relatorio)
        tipo_plataforma = json.dumps(tipo_plataforma)
        status = json.dumps(status)
        dataHora = json.dumps(dataHora)
    
        try:
            relatorio = Relatorio(nomeApp=nomeApp, 
            Mensagem = Mensagem,
            nome_relatorio=nome_relatorio,
            tipo_plataforma=tipo_plataforma,
            dataHora=dataHora,
            status=status)
            db.session.add(relatorio)
            db.session.commit()
            return Response()

        except Exception as erro:
            print("Aqui vai dizer o erro")
            print(erro)
            return False
