
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from random import randint
import random

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


    

    

    