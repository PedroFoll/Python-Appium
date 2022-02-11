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
from variaveisCadastro import*
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
relatorio_Troca_Foto = "relatorio_Troca_Foto.html"

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
      arquivo.write(htmlHead+relatorio_Troca_Foto+htmlFoot)
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
  relatorio_Troca_Foto+="<li>ERRO - Nao foi possível realizar o login</li>"
  gerando_pasta_relatorio()
else:
  print(TerminalColor.SUCCESS+"Tela de login está sendo carregada"+TerminalColor.NORMAL)
  relatorio_Troca_Foto+="<li>SUCESSO - TELA DE LOGIN ESTA SENDO CARREGADA</li>"
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
  relatorio_Troca_Foto+="<li>ERRO - CAMPO PARA INSERIR O E-MAIL NAO FOI ENCONTRADO</li>"
  gerando_pasta_relatorio()
else:
  print(TerminalColor.SUCCESS+"E-mail inserido"+TerminalColor.NORMAL)
  relatorio_Troca_Foto+="<li>SUCESSO - E-MAIL INSERIDO</li>"


try:
  typePassword = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[2]")
except:
  print(TerminalColor.ERRO+'='*40+"\nCampo para inserir a senha não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Troca_Foto+= "<li>ERRO - CAMPO PARA INSERIR A SENHA NAO FOI ENCONTRADO</li>"
  gerando_pasta_relatorio()
else:
  typePassword.send_keys("123456")
  print(TerminalColor.SUCCESS+"Senha inserida"+TerminalColor.NORMAL)
  relatorio_Troca_Foto+="<li>SUCESSO - SENHA INSERIDA</li>"

try:
  botaoLogin=driver.find_element_by_xpath ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel realizar o login \n"+'='*40+TerminalColor.NORMAL)
  relatorio_Troca_Foto+="ERRO - NÃO FOI POSSIVEL REALIZAR O LOGIN"
  gerando_pasta_relatorio()
else:
  botaoLogin.click()
  print(TerminalColor.SUCCESS+"Login Realisado"+TerminalColor.NORMAL)
  relatorio_Troca_Foto+="<li>SUCESSO - LOGIN REALISADO</li>"
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
  relatorio_Troca_Foto+="<li>CAMPO DO TERMO DE USO DA LOCALIZACAO NAO FOI MOSTRADO</li>"
  gerando_pasta_relatorio()
else:
  clickYesLocation.click()
  print(TerminalColor.SUCCESS+"Campo do termo de uso da localização confirmado"+TerminalColor.NORMAL)
  sleep(1)
  relatorio_Troca_Foto+= "<li>SUCESSO - CAMPO DO TERMO DE USO DA LOCALIZACAO CONFIRMADO</li>"


###############################DANDO PERMISSAO DO USO DO LOCAL
def Permissao_Local(webdriver):
  allowWhileUseApp=webdriver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
  return bool (allowWhileUseApp)
espera.until(Permissao_Local)
try:
  clickAgreeUseLocation= driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
except:
  print(TerminalColor.ERRO+'='*40+"\nCampo da permissão do uso da localização não foi mostrado\n"+'='*40+TerminalColor.NORMAL)
  relatorio_Troca_Foto+="<li>ERRO - CAMPO DA PERMISSAO DO USO DA LOCALIZACAO NAO FOI MOSTRADO</li>"
  gerando_pasta_relatorio()
else:
  clickAgreeUseLocation.click()
  print(TerminalColor.SUCCESS+"Permissão do uso da localização do motorista confirmado"+TerminalColor.NORMAL)
  relatorio_Troca_Foto+="<li>SUCESSO - PERMISSAO DO USO DA LOCALIZACAO DO MOTORISTA CONFIRMADO</li>"
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
  relatorio_Troca_Foto+="<li>ERRO - NAO FOI ENCONTRADO O CAMPO PARA PERMISSAO DE LOCALIZACAO</li>"
  gerando_pasta_relatorio()
else:
  sleep(1)
  clickAllowAllTimeButton.click()
  print(TerminalColor.SUCCESS+" Permissão de localização o tempo todo confirmada "+TerminalColor.NORMAL)
  relatorio_Troca_Foto+="<li>SUCESSO - PERMISSAO DE LOCLIAZACAO O TEMPO TODO CONFIRMADA</li>"
print("="*40)

#########################################################################################
#########################################################################################
#########################################################################################




##################################### Webdrivewait #########################################
wdw = WebDriverWait(driver, 15)
sleep(8)
actions=TouchAction(driver).tap(x=970, y=206).perform()
print("="*40+"\nAgora iremos trocar a foto do motorista")
###################################ENTRANDO NO PERFI DO MOTORISTA###############################
def Botao_Profile(webdriver):
    profileButton=webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View") 
    return bool (profileButton)
wdw.until(Botao_Profile)
try:
    profileClick=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View")
    sleep(2)
except:
    print(TerminalColor.ERRO+'='*40+"\nBotão para abrir o profile não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
    relatorio_Troca_Foto+="<li>ERRO - BOTÃO PARA ABRIR O PROFILE NÃO FOI ENCONTRADO</li>"
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
    relatorio_Troca_Foto+="<li>ERRO - NÃO FOI POSSIVEL ACESSO O MENU DE PERFIL</li>"
    gerando_pasta_relatorio()
else:
    clickEditProfileButton.click()
    print(TerminalColor.SUCCESS+"Foi possivel acesso o menu de perfil"+TerminalColor.NORMAL)
#####################################################################################################



##############################Função para Solicitar a alteração de imagem###########################
def Trocando_Foto(webdriver):
    buttonChangePhoto=webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]")
    return bool(buttonChangePhoto)
wdw.until(Trocando_Foto)
try:
    changeFoto=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]")
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - Campo para troca de imagem não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
    relatorio_Troca_Foto += "<li>ERRO - Campo para troca de imagem não foi encontrado</li>"
    gerando_pasta_relatorio()
else:
    changeFoto.click()
    print(TerminalColor.SUCCESS+"SUCESSO - A camera para troca de imagem está sendo aberta"+TerminalColor.NORMAL)
    relatorio_Troca_Foto += "<li>SUCESSO - A camera para troca de imagem está sendo aberta</li>"

#################################Função para permitir midia
def Permitindo_Midia(webdriver):
    allowUseMidia=webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")
    return bool (allowUseMidia)
wdw.until(Permitindo_Midia)
try:
    clickAgreeButton=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - Campo de confirmar midia não encontrado\n"+'='*40+TerminalColor.NORMAL)
    relatorio_Troca_Foto+= "<li>ERRO - Campo de confirmar midia não encontrado</li>"
    gerando_pasta_relatorio()
else:
    clickAgreeButton.click()
    print(TerminalColor.SUCCESS+"SUCESSO - Permissão de midia confirmada"+TerminalColor.NORMAL)
    relatorio_Troca_Foto+= "<li>SUCESSO - Permissão de midia confirmada</li>"

############################################BATENDO A FOTO
def Batendo_Fotos(webdriver):
    toTakePicture = webdriver.find_element_by_xpath(cammeraButton)
    return bool (toTakePicture)
wdw.until(Batendo_Fotos)
try:
    sleep(3)
    takeFoto=driver.find_element_by_xpath(cammeraButton).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel bater nenhuma foto \n"+'='*40+TerminalColor.NORMAL)
    relatorio_Troca_Foto+= "<li>ERRO - Não foi possivel bater nenhuma foto</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - FOTO BATIDA "+TerminalColor.NORMAL)
    relatorio_Troca_Foto+= "<li>SUCESSO - FOTO BATIDA</li>"

#ENVIANDO A FOTO
def Enviando_Foto(webdriver):
    toSendPicture = webdriver.find_element_by_xpath(photoConfirm)
    return bool(toSendPicture)
wdw.until(Enviando_Foto)
try:
    sleep(3)
    sendFoto=driver.find_element_by_xpath(photoConfirm)
    sendFoto.click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível enviar a foto\n"+'='*40+TerminalColor.NORMAL)
    relatorio_Troca_Foto+= "<li>ERRO - Não foi possível enviar a foto</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - Foto batida e enviada"+TerminalColor.NORMAL)
    relatorio_Troca_Foto+="<li>SUCESSO - FOTO BATIDA E ENVIADA</li>"

def Confirmar_Envio(webdriver):
    toConfirmPhotoSent = webdriver.find_element_by_xpath(confirmPictureSend)
    return bool (toConfirmPhotoSent)
wdw.until(Confirmar_Envio)
try:
    sleep(3)
    clickConfirmSent = driver.find_element_by_xpath(confirmPictureSend).click()
except:
    print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível enviar a foto\n"+'='*40+TerminalColor.NORMAL)
    relatorio_Troca_Foto+= "<li>ERRO - Não foi possível enviar a foto</li>"
    gerando_pasta_relatorio()
else:
    print(TerminalColor.SUCCESS+"SUCESSO - Foto batida e enviada"+TerminalColor.NORMAL)
    relatorio_Troca_Foto+="<li>SUCESSO - FOTO BATIDA E ENVIADA</li>"
gerando_pasta_relatorio()
#############################################SCRIPT FEITO POR PEDRO FOLL