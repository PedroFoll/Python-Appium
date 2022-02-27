from array import array
from inspect import _void
from logging import WARN
from sre_constants import SUCCESS
from variaveisAceitandoCorridas import*
from variaveisProfileMenu import*
from appium.webdriver import Remote
from appium.webdriver.extensions.search_context import android
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from variaveisProfileMenu import*
from A12_Enviando_Mensagem import*
from datetime import datetime
data = (str(datetime.now()))
#Desire caps
link_App = input("Informe seu app\n")

""" driver= Remote( 
        'http://localhost:4723/wd/hub',
{
  "platformName": "android",
  "appium:deviceName": "AppiumP",
  "appium:app": link_App,
  "appium:avd": "Pixel_5_API_29_2",
  "isHeadless": True,
  "avdArgs":"no-window"
})
 """
htmlHead = '<!DOCTYPE html><html lang="bt-BR"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Relatório Teste</title><h1>Teste de Relatório</h1><h3>Itens testados</h3><ul>'
htmlFoot = '</ul></body></html>'

print('='*40+'Nome do Relatório (app):')
x= input()
print('='*40+'Deseja testar Android(1) ios(2)')
y= input()
print('='*40+'Iniciando, ' + x)

class TerminalColor:
    SUCCESS = '\033[32m' #Verde
    ERRO = '\033[91m' #Vermelho
    NORMAL = '\033[0m' #Branco
    WARN = '\033[33m' #Amarelo
x = "Inicio do relatorio"
#####################BUSCANDO DATA E HORA PARA CRIAÇÃO DA PASTA E RELATORIO
data_hora = (datetime.now())
data = data_hora.strftime("%d-%m-%Y")
hora = data_hora.strftime("%H_%M_%S")
print("Data atual e hora é")
print(" "+data +" "+hora)  

##############################################################################

x = "Inicio do relatorio"
espera = WebDriverWait (driver,15)

####################################INICIANDO CORRIDA###################################
def Iniciando_Corrida(webdriver):
    startTrip = webdriver.find_element_by_xpath(slideButton)
    return bool (startTrip)
espera.until(Iniciando_Corrida)
try:
    element_to_tap = driver.find_element_by_xpath(slideButton)
    element_to_drag_to = driver.find_element_by_xpath(arrowIcon)
except:
    print(TerminalColor.ERRO+'='*40+"\n \n"+'='*40+TerminalColor.NORMAL)
    x +="\n"
else: 
    print(TerminalColor.SUCCESS+" "+TerminalColor.NORMAL)
    x +="\n"
#########################################################################################


##################################FINALIZANDO CORRIDA###################################
def Finalizando_Corrida(webdriver):
    finishTrip = webdriver.find_element_by_xpath(slideButton)
    return bool (finishTrip)
espera.until(Finalizando_Corrida)
try:
    element_to_tap = driver.find_element_by_xpath(slideButton)
    element_to_drag_to = driver.find_element_by_xpath(arrowIcon)
except:
    print(TerminalColor.ERRO+'='*40+"\n \n"+'='*40+TerminalColor.NORMAL)
    x +="\n"
else:
    print(TerminalColor.SUCCESS+" "+TerminalColor.NORMAL)
    x +="\n"
#########################################################################################


##########################FECHANDO JANELA DO RESUMO DA VIAGEM###########################
def Fechando_Resumo_Viagem(webdriver):
    closeButton = webdriver.find_element_by_xpath(closeResumTrip)
    return bool (closeButton)
espera.until(Fechando_Resumo_Viagem)
try:
    element_to_tap = driver.find_element_by_xpath(slideButton)
    element_to_drag_to = driver.find_element_by_xpath(arrowIcon)
except:
    print(TerminalColor.ERRO+'='*40+"\n \n"+'='*40+TerminalColor.NORMAL)
    x +="\n"
else:
    print(TerminalColor.SUCCESS+" "+TerminalColor.NORMAL)
    x +="\n"
###########################GERANDO RELATORIOS############################################
with open("x.txt", 'w') as arquivo:
    arquivo.write(x)
#########################################################################################
#######################ESSES CASOS DE TESTES PRECISAM SER REFATORADOS####################
