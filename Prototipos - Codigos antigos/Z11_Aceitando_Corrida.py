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
from variaveisProfileMenu import*
import os
from datetime import datetime
data = (str(datetime.now()))
#Cores para os relatorios no monitor
class TerminalColor:
    SUCCESS = '\033[32m' #Verde
    ERRO = '\033[91m' #Vermelho
    NORMAL = '\033[0m' #Branco
#Desire caps
driver= Remote( 
        'http://localhost:4723/wd/hub',
{
  "platformName": "android",
  "appium:deviceName": "AppiumP",
  "appium:app": sys.argv[1],
  "appium:avd": "Nexus_5_API_29",
  "isHeadless": True,
  "avdArgs":"no-window"
})
relatorio_Aceitando_Corrida = " "

htmlHead = '<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Relatório Teste</title><h1>Teste de Relatório</h1><h3>Itens testados</h3><ul>'
htmlFoot = '</ul></body></html>'

x= sys.argv[2]
y= sys.argv[3]
print('Nome do Relatório (app):'+x)
if y == "1":
  print('Seu teste será iniciado em Android')
else:
  print('Seu teste será iniciado em IOS')
print('Iniciando, ' + x)

#####################BUSCANDO DATA E HORA PARA CRIAÇÃO DA PASTA E RELATORIO
data_hora = (datetime.now())
data = data_hora.strftime("%d-%m-%Y")
hora = data_hora.strftime("%H_%M_%S")
print("Teste iniciado")
print("no dia: "+data +" às "+hora)
####################################################################################
def gerando_pasta_relatorio():
  if os.path.isdir("C:/Users/pedro/Documents/testemobile/Relatorios/"+x): # vemos de este diretorio ja existe
    print ('Ja existe uma pasta com esse nome!')
  else:
    os.mkdir("C:/Users/pedro/Documents/testemobile/Relatorios/"+x+" "+data+" "+hora) # aqui criamos a pasta caso nao exista
    with open("C:/Users/pedro/Documents/testemobile/Relatorios/"+x+" "+data+" "+hora+"/"+x+".html", 'w') as arquivo:
      arquivo.write("Teste realizado\n"+data+"<li></li>")
      arquivo.write(htmlHead+relatorio_Aceitando_Corrida+htmlFoot)
      print ('Pasta criada com sucesso!')
  sys.exit()

####################################################################################

####################################LOGANDO MOTORISTA
espera = WebDriverWait (driver,20)
def Clicando_Para_Logar(webdriver):
  clickLoginButton = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]")
  return bool (clickLoginButton)
espera.until(Clicando_Para_Logar)
try:
  clicklogin = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]")
  clicklogin.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel Realizar o login\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>ERRO - Nao foi possível realizar o login</li>"
  gerando_pasta_relatorio()
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Tela de login está sendo carregada"+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>SUCESSO - TELA DE LOGIN ESTA SENDO CARREGADA</li>"
  sleep(1)


####################################INSERINDO E-MAIL E SENHA
def Inserindo_Email_Senha(webdriver):
  emailM = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[1]")
  return bool (emailM)
espera.until(Inserindo_Email_Senha)
print(TerminalColor.NORMAL+"="*40+"\nTela para login")

try:
  typeEmailM = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[1]")
  typeEmailM.send_keys("peddro.foll@gmail.com")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo para inserir o E-mail não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>ERRO - CAMPO PARA INSERIR O E-MAIL NAO FOI ENCONTRADO</li>"
  gerando_pasta_relatorio()
else:
  print(TerminalColor.SUCCESS+"SUCESSO - E-mail inserido"+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>SUCESSO - E-MAIL INSERIDO</li>"


try:
  typePassword = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[2]")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo para inserir a senha não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+= "<li>ERRO - CAMPO PARA INSERIR A SENHA NAO FOI ENCONTRADO</li>"
  gerando_pasta_relatorio()
else:
  typePassword.send_keys("123456")
  print(TerminalColor.SUCCESS+"SUCESSO - Senha inserida"+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>SUCESSO - SENHA INSERIDA</li>"

try:
  botaoLogin=driver.find_element_by_xpath ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel realizar o login \n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="ERRO - NÃO FOI POSSIVEL REALIZAR O LOGIN"
  gerando_pasta_relatorio()
else:
  botaoLogin.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Login Realisado"+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>SUCESSO - LOGIN REALISADO</li>"
  sleep(10)

####################################ACEITANDO E DANDO PERMISSÕES
def Aceitando_Permissoes(webdriver):
  useLocation=webdriver.find_element_by_xpath("//android.view.View[@resource-id='optionAcceptedLocalBackground']")
  return bool (useLocation)
espera.until(Aceitando_Permissoes)
print(TerminalColor.NORMAL+"="*40+"\nDando as permissoes ao App")
try:
  clickYesLocation=driver.find_element_by_xpath("//android.view.View[@resource-id='optionAcceptedLocalBackground']")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo do termo de uso da localização não foi mostrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>ERRO - CAMPO DO TERMO DE USO DA LOCALIZACAO NAO FOI MOSTRADO</li>"
  gerando_pasta_relatorio()
else:
  clickYesLocation.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Campo do termo de uso da localização confirmado"+TerminalColor.NORMAL)
  sleep(1)
  relatorio_Aceitando_Corrida+= "<li>SUCESSO - CAMPO DO TERMO DE USO DA LOCALIZACAO CONFIRMADO</li>"


###############################DANDO PERMISSAO DO USO DO LOCAL
def Permissao_Local(webdriver):
  allowWhileUseApp=webdriver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
  return bool (allowWhileUseApp)
espera.until(Permissao_Local)
try:
  clickAgreeUseLocation= driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo da permissão do uso da localização não foi mostrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>ERRO - CAMPO DA PERMISSAO DO USO DA LOCALIZACAO NAO FOI MOSTRADO</li>"
  gerando_pasta_relatorio()
else:
  clickAgreeUseLocation.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Permissão do uso da localização do motorista confirmado"+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>SUCESSO - PERMISSAO DO USO DA LOCALIZACAO DO MOTORISTA CONFIRMADO</li>"
  sleep(10)

##################################Permissão de localização o tempo todo
def Permissao_All_Time(webdriver):
  allowAllTimeButton = webdriver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")
  return bool (allowAllTimeButton)
espera.until(Permissao_All_Time)
try:
  clickAllowAllTimeButton = driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi encontrado o campo\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>ERRO - NAO FOI ENCONTRADO O CAMPO PARA PERMISSAO DE LOCALIZACAO</li>"
  gerando_pasta_relatorio()
else:
  sleep(1)
  clickAllowAllTimeButton.click()
  print(TerminalColor.SUCCESS+" SUCESSO - Permissão de localização o tempo todo confirmada "+TerminalColor.NORMAL)
  relatorio_Aceitando_Corrida+="<li>SUCESSO - PERMISSAO DE LOCLIAZACAO O TEMPO TODO CONFIRMADA</li>"
print("="*40)
sleep(10)
#########################################################################################
###########################################FIM DO LOGIN##################################
#########################################################################################


#########################################################################################
############################FICANDO ONLINE e ACEITANDO CORRIDAS##########################
#########################################################################################
print("Começando teste de ficar online")
def Ficando_Online(webdriver):
    findStartButton = webdriver.find_element_by_xpath(startButton)
    return bool (findStartButton)
espera.until(Ficando_Online)
try:
    clickStarting = driver.find_element_by_xpath(startButton).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - BOTÃO PARA FICAR ONLINE NÃO ENCONTRADO\n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida+="<li>ERRO - BOTÃO PARA FICAR ONLINE NÃO ENCONTRADO</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - MOTORISTA ONLINE "+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida+="<li>SUCESSO - MOTORISTA ONLINE</li>"
print("Finalizando")
##############################################################################################


############################SOBREPOSIÇÃO EM OUTROS APPS#######################################
def Aceitar_Sobreposição (webdriver):
    findOverOtherAppsButton = webdriver.find_element_by_xpath(overOtherApps)
    return bool (findOverOtherAppsButton)
espera.until(Aceitar_Sobreposição)
try:
    sleep(3)
    clickOverOtherAppsButton =driver.find_element_by_xpath(overOtherApps).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível aceitar a sobreposição \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>ERRO - Não foi possível aceitar a sobreposição</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"\nSUCESSO - ")
    relatorio_Aceitando_Corrida +="<li>SUCESSO - </li>"
############################ACEITANDO CORRIDA#################################################
def Aceitando_Corrida(webdriver):
    beCallingByClient = webdriver.find_element_by_xpath(callTrip)
    return bool (beCallingByClient)
espera.until(Aceitando_Corrida)
try:
    calledByClient = driver.find_element_by_xpath(callTrip).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO EXISTE CORRIDA DISPONIVEL \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>ERRO - NÃO EXISTE CORRIDA DISPONIVEL</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO -  "+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>SUCESSO - </li>"
##############################################################################################
###################A FORMA QUE SERÁ REALIZADO O SEGUINTE PROCEDIMENTO###################
##################PODE NÃO SER A MELHOR FORMA QUE POSSA SER UTILIZADA MAS###############
####################FOI COMO EU CONSEGUI REALIZAR OS SEGUINTES TESTES####################


############################SINALIZANDO CHEGADA AO CLIENTE##############################
def Sinalizando_Chegada(webdriver):
    arrivalSignal = webdriver.find_element_by_xpath(slideButton)
    return bool (arrivalSignal)
espera.until(Sinalizando_Chegada)
try:
    slideArrivalSignal =driver.find_element_by_xpath(slideButton)
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>ERRO - </li>"
    gerando_pasta_relatorio()
else:
    actions = TouchAction(driver)
    actions.press(x=144, y=2036) 
    actions.move_to(x=798, y=2033) 
    actions.release() 
    actions.perform()
    print(TerminalColor.SUCCESS+"SUCESSO -  "+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>SUCESSO - </li>"
#########################################################################################


####################################INICIANDO CORRIDA###################################
def Iniciando_Corrida(webdriver):
    startTrip = webdriver.find_element_by_xpath(slideButton)
    return bool (startTrip)
espera.until(Iniciando_Corrida)
try:
    slideStartTrip = driver.find_element_by_xpath(slideButton)
except:
    print(TerminalColor.ERRO+'='*40+"\n \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li></li>"
    gerando_pasta_relatorio()
else: 
    actions = TouchAction(driver)
    actions.press(x=144, y=2036) 
    actions.move_to(x=798, y=2033) 
    actions.release() 
    actions.perform()
    print(TerminalColor.SUCCESS+"SUCESSO - "+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>SUCESSO - </li>"
#########################################################################################


##################################FINALIZANDO CORRIDA###################################
def Finalizando_Corrida(webdriver):
    finishTrip = webdriver.find_element_by_xpath(slideButton)
    return bool (finishTrip)
espera.until(Finalizando_Corrida)
try:
    slidefinishTrip = driver.find_element_by_xpath(slideButton)
except:
    print(TerminalColor.ERRO+'='*40+"\n \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li></li>"
    gerando_pasta_relatorio()
else: 
    actions = TouchAction(driver)
    actions.press(x=144, y=2036) 
    actions.move_to(x=798, y=2033) 
    actions.release() 
    actions.perform()
    print(TerminalColor.SUCCESS+"SUCESSO - "+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>SUCESSO - </li>"
#########################################################################################


##########################FECHANDO JANELA DO RESUMO DA VIAGEM###########################
def Fechando_Resumo_Viagem(webdriver):
    closeButton = webdriver.find_element_by_xpath(closeResumTrip)
    return bool (closeButton)
espera.until(Fechando_Resumo_Viagem)
try:
    clickCloseButton = driver.find_element_by_xpath(closeResumTrip).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nSUCESSO - \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>SUCESSO - </li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - "+TerminalColor.NORMAL)
    relatorio_Aceitando_Corrida +="<li>SUCESSO - </li>"
    gerando_pasta_relatorio()

#########################################################################################
###################################SCRIPT FINALIZADO#####################################
#########################################################################################
