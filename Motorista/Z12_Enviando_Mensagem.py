from array import array
from inspect import _void
from select import select
from variaveisAceitandoCorridas import*
from variaveisProfileMenu import*
import sys
from time import sleep
from appium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from variaveisProfileMenu import*
from A11_Aceitando_Corrida import*
from A1_logandoMotorista_v2 import aberto
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

x = "Inicio do relatorio"
#####################BUSCANDO DATA E HORA PARA CRIAÇÃO DA PASTA E RELATORIO
data_hora = (datetime.now())
data = data_hora.strftime("%d-%m-%Y")
hora = data_hora.strftime("%H_%M_%S")
print("Data atual e hora é")
print(" "+data +" "+hora)
#####################################################################################

x = "Inicio do relatorio"
espera = WebDriverWait (driver,15)

####################################ABRINDO CHAT######################################
def Abrindo_Chat(webdriver):
    openChat = webdriver.find_element_by_xpath(chatBubble)
    return bool (openChat)
espera.until(Abrindo_Chat)
try:
    clickOpenChat = driver.find_element_by_xpath(chatBubble).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO FOI POSSÍVEL ENCONTRAR O CAMPO PARA ABRIR O CHAT\n"+'='*40+TerminalColor.NORMAL)
    x +="\nERRO - NÃO FOI POSSÍVEL ENCONTRAR O CAMPO PARA ABRIR O CHAT"
else:
    print(TerminalColor.SUCCESS+"SUCESSO - CHAT ABERTO "+TerminalColor.NORMAL)
    x +="\nSUCESSO - CHAT ABERTO"
#########################################################################################

##########################UTILIZADO SOMENTE NO PRIMEIRO ACESSO###########################
#############################PERMITINDO AUDIO DO MOTORISTA###############################

if aberto == "0":
    clickAllowAudio = driver.find_element_by_xpath(allowRecordAudio).click()
    print(TerminalColor.SUCCESS+" "+TerminalColor.NORMAL)
    x +="\n"

#########################################################################################    


#############################Escrevendo Mensagem########################################
############################E ENVIANDO A MENSAGEM#######################################
def Escrevendo_Mensagem(webdriver):
    sendMsgField = webdriver.find_element_by_xpath(fieldOfText)
    return bool (sendMsgField)
espera.until(Escrevendo_Mensagem)
try:
    sendMsg = driver.find_element_by_xpath(fieldOfText).send_keys("Olá, estou realizando um teste de mensagens no seu aplicativo")
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO FOI POSSÍVEL INSERIR MENSAGEM \n"+'='*40+TerminalColor.NORMAL)
    x +="\nERRO - NÃO FOI POSSÍVEL INSERIR MENSAGEM"
else:
    print(TerminalColor.SUCCESS+"SUCESSO - MENSAGEM INSERIDA "+TerminalColor.NORMAL)
    x +="\nSUCESSO - MENSAGEM INSERIDA "
    sleep(2)
##############Click de envio da mensagem#############
try:
    clickSendMsg =driver.find_element_by_xpath(toSendTheMsg).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO FOI POSSIVEL ENVIAR A MENSAGEM \n"+'='*40+TerminalColor.NORMAL)
    x +="\nERRO - NÃO FOI POSSIVEL ENVIAR A MENSAGEM"
else:
    print(TerminalColor.SUCCESS+"SUCESSO - A MENSAGEM FOI ENVIADA "+TerminalColor.NORMAL)
    x +="\nSUCESSO - A MENSAGEM FOI ENVIADA"
#############################CERTIFICANDO ENVIO DA MENSAGEM##############################
driver.implicitly_wait(10)
try:   
     ifMsgWasSent = driver.find_element_by_xpath(theSentMsg)
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO FOI POSSIVEL ENGTREGAR A MENSAGEM\n"+'='*40+TerminalColor.NORMAL)
    x +="\nERRO - NÃO FOI POSSIVEL ENTREGAR A MENSAGEM"
else:
    print(TerminalColor.SUCCESS+"SUCESSO - MENSAGEM ENTREGUE"+TerminalColor.NORMAL)
    x +="\nSUCESSO - MENSAGEM ENTREGUE"
    sleep(3)
########################################################################################


#############################VOLTANDO PARA TELA DA CORRIDA##############################
def Voltando_Tela_Corrida(webdriver):
    backButton = webdriver.find_element_by_xpath(toBackButton)
    return bool (backButton)
espera.until(Voltando_Tela_Corrida)
try:
    backButton = driver.find_element_by_xpath(toBackButton).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO FOI POSSIVEL VOLTAR PARA TELA DE VIAGENS\n"+'='*40+TerminalColor.NORMAL)
    x +="\nERRO - NÃO FOI POSSIVEL VOLTAR PARA TELA DE VIAGENS"
else:
    print(TerminalColor.SUCCESS+"SUCESSO - VOLTANDO PARA A TELA DE VIAGEM"+TerminalColor.NORMAL)
    x +="\nSUCESSO - VOLTANDO PARA A TELA DE VIAGEM"
