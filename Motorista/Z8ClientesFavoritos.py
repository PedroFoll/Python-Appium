from inspect import _void
from logging import WARN
from select import select
from sre_constants import SUCCESS
from variaveisAceitandoCorridas import*
from variaveisProfileMenu import*
import sys
from time import sleep
from appium.webdriver import Remote
from appium.webdriver.extensions.search_context import android
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from variaveisProfileMenu import*
from A1_logandoMotorista_v2  import*
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

#####################BUSCANDO DATA E HORA PARA CRIAÇÃO DA PASTA E RELATORIO
data_hora = (datetime.now())
data = data_hora.strftime("%d-%m-%Y")
hora = data_hora.strftime("%H_%M_%S")
print("Data atual e hora é")
print(" "+data +" "+hora)
#####################################################################################

x = "Inicio do relatorio"
espera = WebDriverWait (driver,15)
#Para inciar o processo é necessário clickar no icone do MENU
#Essa ação é para clickar no icone do menu
sleep(6)
actions=TouchAction(driver).tap(x=970, y=206).perform()

def Abrindo_Menu_ClientesFavoritos(webdriver):
    menuClient=webdriver.find_element_by_xpath(favoritedClients)
    return bool (menuClient)
espera.until(Abrindo_Menu_ClientesFavoritos)
try:
    clickFavoritedClient=driver.find_element_by_xpath(favoritedClients).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO FOI POSSIVEL ABRIR O MENU DE CLIENTES FAVORITOS\n"+'='*40+TerminalColor.NORMAL)
    x +="\nERRO - NÃO FOI POSSIVEL ABRIR O MENU DE CLIENTES FAVORITOS"
else:
    print(TerminalColor.SUCCESS+"SUCESSO - MENU DE CLIENTES FAVORITOS ABERTO"+TerminalColor.NORMAL)
    x +="\nSUCESSO - MENU DE CLIENTES FAVORITOS ABERTO"

def Verificiando_Existencia_Cliente(webdriver):
   aClientFavorited=webdriver.find_element_by_xpath(theFavoritedClient)
   return bool (aClientFavorited)
espera.until(Verificiando_Existencia_Cliente)
try:
     theClient=driver.find_element_by_xpath(theFavoritedClient)
except:
    print(TerminalColor.WARN+'='*40+"\nAVISO -NÃO FOI ENCONTRADO NENHUM CLIENTE FAVORITADO\n"+'='*40+TerminalColor.NORMAL)
    x +="\nAVISO -NÃO FOI ENCONTRADO NENHUM CLIENTE FAVORITADO"
else:
    print(TerminalColor.SUCCESS+"SUCESS - CLIENTE FAVORITADO ENCONTRADO"+TerminalColor.NORMAL)
    x +="\nSUCESS - CLIENTE FAVORITADO ENCONTRADO"



with open("RelatorioModelo.txt", 'w') as arquivo:
    arquivo.write(x)
#####################FIM DA BUSCA POR CLIENTES########################
#####################SCRIPT DE TESTE FEITO POR PEDRO##################