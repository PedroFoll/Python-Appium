from inspect import _void
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
import os
from variaveisCadastro import*
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

Relatorio_Troca_Senha=""
htmlHead = '<!DOCTYPE html><html lang="pt-BR><head><meta charset="UTF-8"/><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Relatório Teste</title><h1>Teste de Relatório</h1><h3>Itens testados</h3><ul>'
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
      arquivo.write(htmlHead+Relatorio_Troca_Senha+htmlFoot)
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
  Relatorio_Troca_Senha+="<li>ERRO - Nao foi possível realizar o login</li>"
  gerando_pasta_relatorio
else:
  print(TerminalColor.SUCCESS+"Tela de login está sendo carregada"+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+="<li>SUCESSO - TELA DE LOGIN ESTA SENDO CARREGADA</li>"
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
  Relatorio_Troca_Senha+="<li>ERRO - CAMPO PARA INSERIR O E-MAIL NAO FOI ENCONTRADO</li>"
  gerando_pasta_relatorio()
else:
  print(TerminalColor.SUCCESS+"E-mail inserido"+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+="<li>SUCESSO - E-MAIL INSERIDO<li>"
try:
  typePassword = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[2]")
except:
  print(TerminalColor.ERRO+'='*40+"\nCampo para inserir a senha não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+= "<li>ERRO - CAMPO PARA INSERIR A SENHA NAO FOI ENCONTRADO</li>"
  gerando_pasta_relatorio()
else:
  typePassword.send_keys("123456")
  print(TerminalColor.SUCCESS+"Senha inserida"+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+="<li>SUCESSO - SENHA INSERIDA</li>"

try:
  botaoLogin=driver.find_element_by_xpath ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel realizar o login \n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+="ERRO - NÃO FOI POSSIVEL REALIZAR O LOGIN"
  gerando_pasta_relatorio()
else:
  botaoLogin.click()
  print(TerminalColor.SUCCESS+"Login Realisado"+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+="<li>SUCESSO - LOGIN REALISADO</li>"
  sleep(5)

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
  Relatorio_Troca_Senha+="<li>CAMPO DO TERMO DE USO DA LOCALIZACAO NAO FOI MOSTRADO</li>"
  gerando_pasta_relatorio()
else:
  clickYesLocation.click()
  print(TerminalColor.SUCCESS+"Campo do termo de uso da localização confirmado"+TerminalColor.NORMAL)
  sleep(1)
  Relatorio_Troca_Senha+= "<li>SUCESSO - CAMPO DO TERMO DE USO DA LOCALIZACAO CONFIRMADO</li>"


###############################DANDO PERMISSAO DO USO DO LOCAL
def Permissao_Local(webdriver):
  allowWhileUseApp=webdriver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
  return bool (allowWhileUseApp)
espera.until(Permissao_Local)
try:
  clickAgreeUseLocation= driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
except:
  print(TerminalColor.ERRO+'='*40+"\nCampo da permissão do uso da localização não foi mostrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+="<li>ERRO - CAMPO DA PERMISSAO DO USO DA LOCALIZACAO NAO FOI MOSTRADO</li>"
  gerando_pasta_relatorio()
else:
  clickAgreeUseLocation.click()
  print(TerminalColor.SUCCESS+"Permissão do uso da localização do motorista confirmado"+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+="<li>SUCESSO - PERMISSAO DO USO DA LOCALIZACAO DO MOTORISTA CONFIRMADO</li>"
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
  Relatorio_Troca_Senha+="<li>ERRO - NAO FOI ENCONTRADO O CAMPO PARA PERMISSAO DE LOCALIZACAO</li>"
  gerando_pasta_relatorio()
else:
  sleep(1)
  clickAllowAllTimeButton.click()
  print(TerminalColor.SUCCESS+" Permissão de localização o tempo todo confirmada "+TerminalColor.NORMAL)
  Relatorio_Troca_Senha+="<li>SUCESSO - PERMISSAO DE LOCLIAZACAO O TEMPO TODO CONFIRMADA</li>"
print("="*40)

#########################################################################################
#########################################################################################
#########################################################################################


############################Iniciando Codigo DA TROCA DE SENHA################################
wdw = WebDriverWait(driver, 15)
print("="*40+"\nAgora iremos trocar a senha")
sleep(8)
actions=TouchAction(driver).tap(x=970, y=206).perform()

#Abrindo menu do motorista e acessando o Perfil/Profile
#FUNÇÃO PARA ABRIR A ABA DE PERFIL
def Botao_Profile(webdriver):
    profileButton=webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View") 
    return bool (profileButton)
wdw.until(Botao_Profile)
try:
    profileClick=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View")
    sleep(2)
except:
    print(TerminalColor.ERRO+'='*40+"\nBotão para abrir o profile não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+="<li>ERRO - BOTÃO PARA ABRIR O PROFILE NÃO FOI ENCONTRADO</li>"
    gerando_pasta_relatorio()
else:
    profileClick.click()
    sleep(1)

#FUNÇÃO PARA ABRIR A ABA DE EDITAR PERFIL
def Clickando_EditarPerfil(webdriver):
    editProfileButton=webdriver.find_element_by_xpath("//android.view.View[@resource-id='editProfileDriver']")
    return bool (editProfileButton)
wdw.until(Clickando_EditarPerfil)
try:
    clickEditProfileButton = driver.find_element_by_xpath("//android.view.View[@resource-id='editProfileDriver']")
except:
    print(TerminalColor.ERRO+'='*40+"\n Não foi possivel acessar o menu de Perfil\n"+'='*40+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+="\n ERRO - NAO FOI POSSIVEL ACESSO O MENU DE PERFIL"
    gerando_pasta_relatorio()
else:
    clickEditProfileButton.click()
    print(TerminalColor.SUCCESS+"Foi possivel acesso o menu de perfil"+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+="<li>SUCESSO -Foi possivel acesso o menu de perfil</li> "

#FUNÇÃO PARA INSERIR SENHA ATUAL, NOVA SENHA E CONFIRMAÇÃO DE SENHA
def Preenchendo_Troca_Senha(webdriver):
    keyIcon = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]")
    return bool (keyIcon)
wdw.until(Preenchendo_Troca_Senha)
try:
    changePasswordcurrent=driver.find_element_by_xpath("//android.widget.EditText[@resource-id='currentPassword']")
except:
    print(TerminalColor.ERRO+'='*40+"\nCampo de senha atual foi encontrado\n"+'='*40+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+="\n ERRO - CAMPO DE SENHA ATUAL FOI ENCONTRADO"
    gerando_pasta_relatorio()
else:
    changePasswordcurrent.send_keys('654321')
    print(TerminalColor.SUCCESS+"Senha atual inserida"+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+="<li>SUCESSO - SENHA ATUAL INSERIDA</li>"

#INSERINDO NOVA SENHA
try:
    changePasswordnew=driver.find_element_by_xpath("//android.widget.EditText[@resource-id='newPassword']")
except:
    print(TerminalColor.ERRO+'='*40+"\nNão foi possivel inserir nova senha\n"+'='*40+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+="<li>ERRO - NÃO FOI POSSIVEL INSERIR NOVA SENHA</li>"
    gerando_pasta_relatorio()
else:
    changePasswordnew.send_keys('654321')
    print(TerminalColor.SUCCESS+"Nova senha inserida"+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+="<li>SUCESSO - NOVA SENHA INSERIDA </li>"
#CONFIRMANDO SENHA INSERIDA
try:
    changePasswordconfirm=driver.find_element_by_xpath("//android.widget.EditText[@resource-id='confirmationPassword']")
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - SENHA DE CONFIRMACAO NAO PODE SER INSERIDA\n"+'='*40+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+= "<li>ERRO - SENHA DE CONFIRMACAO NAO PODE SER INSERIDA</li>"
    gerando_pasta_relatorio()
else:
    changePasswordconfirm.send_keys('654321')
    print(TerminalColor.SUCCESS+"Confirmação de senha inserida"+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+= "<li>SUCESSO - CONFIRMACAO DE SENHA INSERIDA</li>"

#APERTANDO BOTÃO DE SALVAR
try:
    clickSavePassword=driver.find_element_by_xpath("//android.widget.Button[@resource-id='btnChangePassword']")
except:
    print(TerminalColor.ERRO+'='*40+"\nNão foi possível salvar a senha\n"+'='*40+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+= "<li>ERRO - NÃO FOI POSSIVEL SALVAR A SENHA</li>"
    gerando_pasta_relatorio()
else:
    clickSavePassword.click()
    print(TerminalColor.SUCCESS+"Senha salva"+TerminalColor.NORMAL)
    Relatorio_Troca_Senha+= "<li>SUCESSO SENHA</li>"
gerando_pasta_relatorio()

#FIM TROCA DE SENHA
#################################GERANDO PASTA E RELATORIO############################################
""" if os.path.isdir("C:/Users/pedro/Documents/testemobile/Relatorios/"+x): # vemos de este diretorio ja existe
    print ('Ja existe uma pasta com esse nome!')
else:
    os.mkdir("C:/Users/pedro/Documents/testemobile/Relatorios/"+x+" "+data+" "+hora) # aqui criamos a pasta caso nao exista
    with open("C:/Users/pedro/Documents/testemobile/Relatorios/"+x+" "+data+" "+hora+"/TESTE_DE_CADASTRO.html", 'w') as arquivo:
        arquivo.write("Teste realizado\n"+data+"\n")
        arquivo.write(htmlHead+Relatorio_Troca_Senha+htmlFoot)
        print ('Pasta criada com sucesso!')
 """
###########################SCRIPT FEITO POR PEDRO FOLL