from inspect import _void
from logging import WARN
from select import select
from variaveisAceitandoCorridas import*
from variaveisProfileMenu import*
import sys
from time import sleep
from appium.webdriver import Remote
from appium.webdriver.extensions.search_context import android
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from variaveisProfileMenu import*
import os
from datetime import datetime
driver= Remote( 
        'http://localhost:4723/wd/hub',
{
  "platformName": "android",
  "appium:deviceName": "AppiumP",
  "appium:avd": "Nexus_5_API_29",
})
espera = WebDriverWait (driver,15)

""" teste_Relatorio = ("Estou tentando um relatorio em txt\n")
Nome_App = input("Digite o nome do app\n")

data_hora = (datetime.now())
data = data_hora.strftime("%d-%m-%Y")
hora = data_hora.strftime("%H_%M_%S")
print("Data atual e hora é")
print(" "+data +" "+hora) """
#print(data.strftime("%y-%m-%d %H:%M:%S"))
""" 
if os.path.isdir("C:/Users/pedro/Documents/testemobile/Relatorios/"+Nome_App): # vemos de este diretorio ja existe
    print ('Ja existe uma pasta com esse nome!')
else:
    os.mkdir("C:/Users/pedro/Documents/testemobile/Relatorios/"+Nome_App+" "+data+" "+hora) # aqui criamos a pasta caso nao exista
    with open("C:/Users/pedro/Documents/testemobile/Relatorios/"+Nome_App+" "+data+" "+hora+"/TESTE_DE_CADASTRO.txt", 'w') as arquivo:
        arquivo.write("Teste realizado\n"+data+"\n")
        arquivo.write(teste_Relatorio)
        print ('Pasta criada com sucesso!') """

""" class TerminalColor:    
    SUCCESS = '\033[33m' #Verde
    ERRO = '\033[91m' #Vermelho
    NORMAL = '\033[0m' #Branco
print("Se essa for a primeira vez que está abrindo o app digite 0, se já tiver aberto o app, digite 1")
var = input('digite 0 ou 1\n')
if var == 0:
    print("Essa é a primeira vez que vc utiliza o app")
else:
    print("Você já abriu esse app") """

""" print("Tentando o IF")
if overOtherApps == True:
    try:
        clickOverApps = driver.find_element_by_xpath(overOtherApps).click()
        driver.back()
        sleep(5)
    except:
        print("Erro")
    else:
        print("sucesso")
else:
    print("Elemento não encontrado")
    sleep(5) """
print("Entrando função de sobrepor apps")
def sobrepondo_apps(webdriver):
    try:
        clickoverApps = webdriver.find_element_by_xpath(overOtherApps)
        return bool (clickoverApps)
    except:
        None
espera.until(sobrepondo_apps)
print("saiu da função")
try:
    clickOverApps = driver.find_element_by_xpath(overOtherApps).click()
except:
    print("não pegou 2")
else:
    print("Pegou garai")