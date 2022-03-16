
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from random import randint
from geradorRelatorio.geradorRelatorios_Driver import Gerando_Relatorio
import random
from os import sys

class Helpers():

    def gerador_data_hora():
    
        data_hora = (datetime.now())
        data = data_hora.strftime("%d-%m-%Y %H_%M_%S")
        return data


    def gerador_email():

        inicio=(str('teste'))
        final=(str('@teste.com'))               
        meio=(str(random.randint(1,999999)))
        randomMail=(inicio+meio+final)

        return randomMail


    def gerador_telefone():
    
        prefixo = (str(85))
        inicio = (str(99999))
        final = str((randint(1000,9999)))
        numeroCelularAleatorio = (prefixo+inicio+final)
        
        return numeroCelularAleatorio


    def conexao_db(dados, Mensagem,status,nome_relatorio):
        dataHora = Helpers.gerador_data_hora()
        Gerando_Relatorio.gerando_relatorio(nomeApp= dados['nomeApp'], 
                                            nome_relatorio= nome_relatorio,
                                            tipo_plataforma = dados['tipo_plataforma'],
                                            status=status,
                                            dataHora=dataHora,
                                            Mensagem=Mensagem )

    

    