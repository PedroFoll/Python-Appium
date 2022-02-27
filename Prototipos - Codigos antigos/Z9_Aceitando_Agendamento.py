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
relatorio_Aceitando_Agendamento = " "

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
      arquivo.write("Teste realizado\n"+data+"\n")
      arquivo.write(htmlHead+relatorio_Aceitando_Agendamento+htmlFoot)
      print ('Pasta criada com sucesso!')
  sys.exit()


####################################################################################

####################################LOGANDO MOTORISTA
espera = WebDriverWait(driver, 15)
def Clicando_Para_Logar(webdriver):
  clickLoginButton = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]")
  return bool (clickLoginButton)
espera.until(Clicando_Para_Logar)
try:
  clicklogin = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]")
  clicklogin.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nNão foi possivel Realizar o login\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>ERRO - Nao foi possível realizar o login</li>"
  gerando_pasta_relatorio()
else:
  print(TerminalColor.SUCCESS+"Tela de login está sendo carregada"+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>SUCESSO - TELA DE LOGIN ESTA SENDO CARREGADA</li>"
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
  print(TerminalColor.ERRO+'='*40+"\nCampo para inserir o E-mail não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>ERRO - CAMPO PARA INSERIR O E-MAIL NAO FOI ENCONTRADO</li>"
  gerando_pasta_relatorio()
else:
  print(TerminalColor.SUCCESS+"E-mail inserido"+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>SUCESSO - E-MAIL INSERIDO</li>"


try:
  typePassword = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[2]")
except:
  print(TerminalColor.ERRO+'='*40+"\nCampo para inserir a senha não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+= "<li>ERRO - CAMPO PARA INSERIR A SENHA NAO FOI ENCONTRADO</li>"
  gerando_pasta_relatorio()
else:
  typePassword.send_keys("123456")
  print(TerminalColor.SUCCESS+"Senha inserida"+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>SUCESSO - SENHA INSERIDA</li>"

try:
  botaoLogin=driver.find_element_by_xpath ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel realizar o login \n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="ERRO - NÃO FOI POSSIVEL REALIZAR O LOGIN"
  gerando_pasta_relatorio()
else:
  botaoLogin.click()
  print(TerminalColor.SUCCESS+"Login Realisado"+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>SUCESSO - LOGIN REALISADO</li>"
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
  print(TerminalColor.ERRO+'='*40+"\nCampo do termo de uso da localização não foi mostrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>CAMPO DO TERMO DE USO DA LOCALIZACAO NAO FOI MOSTRADO</li>"
  gerando_pasta_relatorio()
else:
  clickYesLocation.click()
  print(TerminalColor.SUCCESS+"Campo do termo de uso da localização confirmado"+TerminalColor.NORMAL)
  sleep(1)
  relatorio_Aceitando_Agendamento+= "<li>SUCESSO - CAMPO DO TERMO DE USO DA LOCALIZACAO CONFIRMADO</li>"


###############################DANDO PERMISSAO DO USO DO LOCAL
def Permissao_Local(webdriver):
  allowWhileUseApp=webdriver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
  return bool (allowWhileUseApp)
espera.until(Permissao_Local)
try:
  clickAgreeUseLocation= driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
except:
  print(TerminalColor.ERRO+'='*40+"\nCampo da permissão do uso da localização não foi mostrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>ERRO - CAMPO DA PERMISSAO DO USO DA LOCALIZACAO NAO FOI MOSTRADO</li>"
  gerando_pasta_relatorio()
else:
  clickAgreeUseLocation.click()
  print(TerminalColor.SUCCESS+"Permissão do uso da localização do motorista confirmado"+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>SUCESSO - PERMISSAO DO USO DA LOCALIZACAO DO MOTORISTA CONFIRMADO</li>"
  sleep(10)

##################################Permissão de localização o tempo todo
def Permissao_All_Time(webdriver):
  allowAllTimeButton = webdriver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")
  return bool (allowAllTimeButton)
espera.until(Permissao_All_Time)
try:
  clickAllowAllTimeButton = driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")
except:
  print(TerminalColor.ERRO+'='*40+"\nNão foi encontrado o campo\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>ERRO - NAO FOI ENCONTRADO O CAMPO PARA PERMISSAO DE LOCALIZACAO</li>"
  gerando_pasta_relatorio()
else:
  sleep(1)
  clickAllowAllTimeButton.click()
  print(TerminalColor.SUCCESS+" Permissão de localização o tempo todo confirmada "+TerminalColor.NORMAL)
  relatorio_Aceitando_Agendamento+="<li>SUCESSO - PERMISSAO DE LOCLIAZACAO O TEMPO TODO CONFIRMADA</li>"
print("="*40)
sleep(10)
#########################################################################################
###########################################FIM DO LOGIN##############################################
#########################################################################################



espera = WebDriverWait (driver,15)
########################PROCURANDO BOTÃO DE FICAR ONLINE E FICANDO ONLINE#################
def Ficando_Online(webdriver):
    buttonStart = webdriver.find_element_by_xpath(startButton)
    return bool (buttonStart)
espera.until(Ficando_Online)
try:
    clickStarting = driver.find_element_by_xpath(startButton).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - BOTÃO START NÃO FOI ENCONTRADO \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>ERRO - BOTÃO START NÃO FOI ENCONTRADO</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - MOTORISTA ONLINE"+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>SUCESSO - CAMPO PARA PERMITIR O USO SOBRE OUTROS APPS ABERTO</li>"
    sleep(10)
####################################################################################################################################
#################################FUNÇÃO PARA SOBREPOR OUTROS APPS####################################################
def sobrepondo_apps(webdriver):
    try:
        clickoverApps = webdriver.find_element_by_xpath(overOtherApps)
        return bool (clickoverApps)
    except:
        print("parou parou parou parou parou parou parou parou")
try:
    clickOverApps = driver.find_element_by_xpath(overOtherApps).click()
except:
    print("SUCESSO - PERMISSAO PARA SOBREPOR APLICATIVOS JA ESTAVA ATIVA")
    relatorio_Aceitando_Agendamento +=("<li>SUCESSO - PERMISSAO PARA SOBREPOR APLICATIVOS JA ESTAVA ATIVA</li>")
else:
    print("SUCESSO - PERSSAO PARA SOBREPOR APLICATIVOS CONCEDIDAs")
    relatorio_Aceitando_Agendamento +=("<li>SUCESSO - PERSSAO PARA SOBREPOR APLICATIVOS CONCEDIDAs</li>")
    driver.back()

############################ACESSANDO TELA DE VIAGENS AGENDADAS###############################
def Acessar_Tela_Viagem_Agendada(webdriver):
    scheduleTripList = webdriver.find_element_by_xpath(scheduleTrip)
    return bool (scheduleTripList)
espera.until(Acessar_Tela_Viagem_Agendada)
try:
    clickScheduleTrip = driver.find_element_by_xpath(scheduleTrip).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO FOI ENCONTRADO NENHUMA CORRIDA AGENDADA\n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>ERRO - NÃO FOI ENCONTRADO NENHUMA CORRIDA AGENDADA</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - EXITEM CORRIDAS AGENDADAS DISPONIVEIS"+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>SUCESSO - EXITEM CORRIDAS AGENDADAS DISPONIVEIS</li>"
##############################################################################################


############################ACEITANDO CORRIDA AGENDADA########################################
def Aceitando_Corrida(webdriver):
    theTrip = webdriver.find_element_by_xpath(acceptTheTrip)
    return bool (theTrip)
espera.until(Aceitando_Corrida)
try:
    clickAcceptTrip = driver.find_element_by_xpath(acceptTheTrip).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - CORRIDA NÃO ESTÁ DISPONIVEL \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>ERRO - CORRIDA NÃO ESTÁ DISPONIVEL</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - CORRIDA ESTÁ DISPONIVEL PARA ACEITAR "+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>SUCESSO - CORRIDA ESTÁ DISPONIVEL PARA ACEITAR</li>"
##############################################################################################


############################CONFIRMANDO ACEITAÇÃO DA CORRIDA##################################
def Confirmando_Corrida_Agendada(webdriver):
    confirmTrip = webdriver.find_element_by_xpath(yesAcceptOrCancelTrip)
    return bool (confirmTrip)
espera.until(Confirmando_Corrida_Agendada)
try:
    clickYesAcceptTrip = driver.find_element_by_xpath(yesAcceptOrCancelTrip).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - NÃO FOI POSSÍVEL CONFIRMAR O ACEITE DA VIAGEM  \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>ERRO - NÃO FOI POSSÍVEL CONFIRMAR O ACEITE DA VIAGEM</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - ACEITE DA VIAGEM CONFIRMADO "+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>SUCESSO - ACEITE DA VIAGEM CONFIRMADO</li>"
##############################################################################################


############################CONFIRMAÇÃO FINAL DE ACEITAÇÃO DA CORRIDA#########################
#################TEMOS VARIAS CERTIFICAÇÕES DE ACEITE/CANCELMANTO NESSE PROCESSO##############
def Confirmação_Final_Aceitando_Corrida(webdriver):
    okAfterAcceptTrip = driver.find_element_by_xpath(afterAcceptedOrCancelTrip)
    return bool (okAfterAcceptTrip)
espera.until(Confirmação_Final_Aceitando_Corrida)
try:
    clickOkAfterAcceptTrip = driver.find_element_by_xpath(afterAcceptedOrCancelTrip).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - BOTÃO DE OK NÃO IDENTIFICADO  \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>ERRO - BOTÃO DE OK NÃO IDENTIFICADO</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - VOCÊ ACEITOU A VIAGEM "+TerminalColor.NORMAL)
    relatorio_Aceitando_Agendamento +="<li>SUCESSO - VOCÊ ACEITOU A VIAGEM</li>"
    gerando_pasta_relatorio()
##############################################################################################
#################################SCRIPT FINALIZADO #############################################
##############################################################################################