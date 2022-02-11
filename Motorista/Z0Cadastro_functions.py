#!/Users/pedro/AppData/Local/Programs/Python/Python310
from inspect import _void
#Não existe error
import re
import os
from select import select
from sre_constants import SUCCESS
from variaveisAceitandoCorridas import*
from variaveisProfileMenu import*
from gerador_cpf import*
from gerador_telefone import numeroCelularAleatorio
import sys
from time import sleep
from appium.webdriver import Remote
from appium.webdriver.extensions.search_context import android
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
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

Relatorio_Cadastro_Motorista = "Inicio do relatorio"
#####################BUSCANDO DATA E HORA PARA CRIAÇÃO DA PASTA E RELATORIO
data_hora = (datetime.now())
data = data_hora.strftime("%d-%m-%Y")
hora = data_hora.strftime("%H_%M_%S")
print("Teste iniciado")
print("no dia: "+data +" às "+hora)
####################################################################################

#WAIT WEB DRIVER
wdw = WebDriverWait(driver, 15)
def Clicando_Para_Registrar(webdriver):
    clickButton = webdriver.find_element_by_xpath(register)
    return bool (clickButton)
wdw.until(Clicando_Para_Registrar)

#ESCOLHE BOTÃO PARA PODER SE CADASTRAR
try:
  clickButton = driver.find_element_by_xpath(register)
  sleep(1)
  clickButton.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel entrar no cadastro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Não foi possivel entrar no cadastro</li>"
  with open("C:/Users/pedro/Documents/TESTE_DE_CADASTRO.txt", 'w') as arquivo:
    arquivo.write(Relatorio_Cadastro_Motorista+"\n"+data)
  sys.exit()
else:
  print(TerminalColor.SUCCESS+'='*40+"\nSUCESSO - Foi possivel entrar no cadastro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - Foi possivel entrar no cadastro</li>"

#TIPOS DE MOTORISTA
def Carregando_Tipos(webdriver):
  clickDriverType=webdriver.find_element_by_xpath(driverType)
  return bool (clickDriverType)
wdw.until(Carregando_Tipos)
try:
  clickDriverType = driver.find_element_by_xpath(driverType).click()
  sleep(3)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi encontrado o campo para selecionar o tipo de motorista\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Não foi encontrado o campo para selecionar o tipo de motorista</li>"
  sys.exit()
else:
  print(TerminalColor.SUCCESS+'='*40+"\nSUCESSO - O tipo de motorista foi selecionado com sucesso\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - O tipo de motorista foi selecionado com sucesso</li>"

#DADOS PESSOAIS
def Dados_Pessoais(webdriver):
  fieldName = webdriver.find_element_by_xpath(toTypeName)
  return bool (fieldName)
wdw.until(Dados_Pessoais)
#PREENCHENDO DADOS PESSOAIS
print('='*40+"\nCadastro dos dados pessoais do motorista")


#Campo Nome
try:
  fieldName = driver.find_element_by_xpath(toTypeName)
  sleep(1)
  fieldName.click()
  fieldName.send_keys("Homologação Fb704")
  nextButton01=driver.find_element_by_xpath(nextButton00)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo de nome não encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Campo de nome não encontrado</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Nome inserido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - Nome inserido</li>"
  nextButton01=driver.find_element_by_xpath(nextButton00)
  nextButton01.click()

#Campo CPF
try:
  fieldCPF = driver.find_element_by_xpath(toTypeCpf)
  fieldCPF.send_keys(cpf_validado)
  fieldCPF.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo de CPF não encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Campo de CPF não encontrado</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - CPF inserido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - CPF inserido</li>"
  nextButton01.click()


#Campo Email
try:
  emailField = driver.find_element_by_xpath(toTypeEmail)
  emailField.send_keys(randoMail)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo de Email não encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Campo de Email não encontrado</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Email inserido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - Email inserido</li>"
  nextButton01.click()


#Campo de telefone
try:
  numberField= driver.find_element_by_xpath(toTypePhone)
  numberField.send_keys(numeroCelularAleatorio)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo de Telefone não encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Campo de Telefone não encontrado</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Telefone inserido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - Telefone inserido</li>"


#FUNÇÃO - DEFINIDO O GENERO
try:
  genderField1= driver.find_element_by_xpath(toSetGender1)
  genderField1.click()
  sleep(3)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo para selecionar Genero não encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Campo para selecionar Genero não encontrado</li>"
try:
  genderField2 = driver.find_element_by_xpath(toSetGender2)
  genderField2.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo de Genero não encontrado"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Campo de Genero não encontrado</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Genero foi definido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - Genero foi definido</li>"
  nextButton01.click()

#FUNÇÃO - INSERINDO SENHA E CONFIRMANDO
def Inserindo_Senha(webdriver):
  passField = webdriver.find_element_by_xpath(toTypePassword)
  return bool(passField)
wdw.until(Inserindo_Senha)

try:
  passWordField=driver.find_element_by_xpath(toTypePassword)
  passWordField.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - O Campo de password não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - O Campo de password não foi encontrado</li>"
try:
  confirmPassWordField=driver.find_element_by_xpath(toConfirmPassword)
  confirmPassWordField.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - O Campo para confirmar o password não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="\nERRO - O Campo para confirmar o password não foi encontrado"
  sys.exit()
else:
  print(TerminalColor.SUCCESS+"\n SUCESSO - A senha foi inserida"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - A senha foi inserida</li>"
  passWordField.send_keys("123456")
  confirmPassWordField.send_keys("123456")
  nextButton= driver.find_element_by_xpath(toContinue)
  nextButton.click()

#FUNÇÃO - DEFININDO A CIDADE
def Selecionando_Cidade(webdriver):
  selectCity1=webdriver.find_element_by_xpath(citySelector1)
  return bool(selectCity1)
wdw.until(Selecionando_Cidade)
try:
  selectCity1=driver.find_element_by_xpath(citySelector1)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo de definir a cidade não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Campo de definir a cidade não foi encontrado</li>"
else:
  selectCity1.click()
  sleep(3)
try:
  selectCity2=driver.find_element_by_xpath(citySelector2)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - O Campo para definir a cidade não apareceu\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - O Campo para definir a cidade não apareceu</li>"
  sys.exit()
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Sua Cidade foi definida com sucesso"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - Sua Cidade foi definida com sucesso</li>"
  selectCity2.click()
  nextButton= driver.find_element_by_xpath(toContinue)
  nextButton.click()


#FUNÇÃO PARA ACEITAR OS TERMOS DE USO
def Aceitando_Termos(webdriver):
  termsScreen=webdriver.find_element_by_xpath(termsTitle)
  return bool (termsScreen)
wdw.until(Aceitando_Termos)
actions = TouchAction(driver)
actions.press(x=14, y=384)
actions.move_to(x=327, y=100)
actions.release() 
actions.perform()
sleep(1)
try:
  checkBoxTermos=driver.find_element_by_xpath(useTerms)
  checkBoxTermos.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível aceitar os termos\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Não foi possível aceitar os termos</li>"
  sys.exit()
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Termos aceitos"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - Termos aceitos</li>"
  nextButton= driver.find_element_by_xpath(toContinue)
  nextButton.click()
  sleep(5)


#FUNÇÃO PARA ENVIAR UMA FOTO DE PERFIL
def Enviar_Foto(webdriver):
  openCamera=webdriver.find_element_by_xpath(toAcessCamera)
  return bool (openCamera)
wdw.until(Enviar_Foto)
print('='*40+"\nFoto de Perfil do Motorista")
try:
  openingCamera=driver.find_element_by_xpath(toAcessCamera).click()
  sleep(2)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível encontrar o campo para envio de fotos\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - Não foi possível encontrar o campo para envio de fotos</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Acessando a camera"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - Acessando a camera</li>"
  sleep(5)

#DANDO PERMISSÃO PARA ACESSAR A CAMER (SÓ PRECISA SER USADO 1 VEZ)
def Aceitando_Permissao_Camera(webdriver):
  toAllowCamera = webdriver.find_element_by_xpath(allowCamera)
  return bool(toAllowCamera)
wdw.until(Aceitando_Permissao_Camera)

try:
  aceptCameraAllow=driver.find_element_by_xpath(allowCamera).click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel dar acesso a camera do seu telefone\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSIVEL DAR ACESSO A CAMERA DO SEU TELEFONE</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Acesso a Camera permitido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - ACESSO A CAMERA PERMITIDO</li>"

#BATENDO A FOTO E ENVIANDO
#BATENDO A FOTO
def Batendo_Fotos(webdriver):
  toTakePicture = webdriver.find_element_by_xpath(cammeraButton)
  return bool (toTakePicture)
wdw.until(Batendo_Fotos)
try:
  takeFoto=driver.find_element_by_xpath(cammeraButton)
except:
  print(TerminalColor.ERRO+'='*40+"\n Não foi possivel bater nenhuma foto \n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL BATER NENHUMA FOTO</li>"
else:
  takeFoto.click()
#ENVIANDO A FOTO
def Enviando_Foto(webdriver):
  toSendPicture = webdriver.find_element_by_xpath(photoConfirm)
  return bool(toSendPicture)
wdw.until(Enviando_Foto)
try:
  sendFoto=driver.find_element_by_xpath(photoConfirm)
  sendFoto.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível enviar a foto\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL ENVIAR A FOTO</li>"
  sys.exit()
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Foto batida e enviada"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - FOTO BATIDA E ENVIADA</li>"

def Indo_Para_Dados(webdriver):
  clickNextButton=webdriver.find_element_by_xpath(toContinue)
  return bool (clickNextButton)
wdw.until(Indo_Para_Dados)
try:
  nextButton= driver.find_element_by_xpath(toContinue)
  nextButton.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO -Não foi possível ir para a tela de Dados do carro \n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL IR PARA A TELA DE DADOS DO CARRO</li>"
  sys.exit()
#=======================================================================================================================
#FUNÇÃO PARA ENVIAR OS DADOS DO CARRO
def Enviando_Dados_Carro(webdriver):
  findBrandField=webdriver.find_element_by_xpath(vehicleBrand)
  return bool (findBrandField)
wdw.until(Enviando_Dados_Carro)
print('='*40+"\nDados do carro")
#INSERIR MARCA DO CARRO
try:
  toTypeVehicleBrand=driver.find_element_by_xpath(vehicleBrand)
  toTypeVehicleBrand.send_keys("Fiat")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível exibir o campo de Marca do carro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL EXIVIR O CAMPO DE MARCA DO CARRO</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Marca inserida"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - MARCA INSERIDA</li>"
#INSERINDO MODELO DO CARRO
try:
  toTypeVehicleModel=driver.find_element_by_xpath(vehicleModel)
  toTypeVehicleModel.send_keys("Uno da 704Apps")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível exibir o campo de Modelo do carro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL EXIBIR O CAMPO DE MODELO DO CARRO</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Modelo inserido "+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - MODELO INSERIDO</li>"
#INSERIDO A PLACA DO CARRO
try:
  toTypeVehiclePlate=driver.find_element_by_xpath(vehiclePlate)
  toTypeVehiclePlate.send_keys("TST-0704")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível exibir o campo para inserir a placa do carro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL EXIBIR O CAMPO PARA INSERIR A PLACA DO CARRO</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Placa inserida "+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - PLACA INSERIDA</li>"
#INSERINDO O RENAVAM DO CARRO
try:
  toTypeVehicleVinNumber=driver.find_element_by_xpath(vehicleVinNumber)
  toTypeVehicleVinNumber.send_keys("12171174856")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível exibir o campo de Renavam \n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL EXIVIR O CAMPO DE RENAVAM</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Renavam inserido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - RENAVAM INSERIDO</li>"

#INSERINDO A COR DO CARRO
try:
  toTypeVehicleColor=driver.find_element_by_xpath(vehicleColor)
  toTypeVehicleColor.send_keys('Azul')
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO -Não foi possível exibir o campo para inserir a cor do carro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL EXIBIR O CAMPO PARA INSERIR A COR DO CARRO</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Cor inserida "+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - COR INSERIDA</li>"
#INSERINDO O NUMERO DE ASSENTOS
try:
  toTypeSeatsNumber=driver.find_element_by_xpath(vehicleSeatsNumber)
  toTypeSeatsNumber.send_keys('5')
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível exibir o campo sobre o numero de assentos\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL EXIBIR O CAMPO SOBRE O NUMERO DE ASSENTOS</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Numero de assentos inserido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - NUMERO DE ASSENTOS INSERIDO</li>"
#INSERINDO ANO DE FABRICAÇÃO DO CARRO
try:
  toTypeVehicleYear=driver.find_element_by_xpath(vehicleYear)
  toTypeVehicleYear.send_keys('2018')
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível exibir o campo do Ano do carro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL EXIBIR O CAMPO DO ANO DO CARRO</li>"
  sys.exit()
else:
  print(TerminalColor.SUCCESS+"SUCESSO -Ano inserido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - ANO INSERIDO</li>"
#PASSANDO PARA A PROXIMA ETAPA
try:
  nextButton= driver.find_element_by_xpath(toContinue)
  nextButton.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível prosseguir para a tela de documentos\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL PROSSEGUIR PARA A TELA DE DOCUMENTOS</li>"
#======================================================================================================================================
#FUNÇÃO PARA ENVIAR FOTOS DA CNH
def Enviar_Documentos(webdriver):
  findCnhField=webdriver.find_element_by_xpath(toTypeCnhField)
  return bool (findCnhField)
wdw.until(Enviar_Documentos)
print('='*40+"\nEnviando fotos da documentção do motorista")
#DIGITANDO CNH
try:
  toTypeCnh=driver.find_element_by_xpath(toTypeCnhField)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi apresentado o campo de CNH\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI APRESENTADO O CAMPO DE CNH</li>"
else:
  toTypeCnh.send_keys("69432109613")
  print(TerminalColor.SUCCESS+"SUCESSO - CNH Inserido "+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - CHN INSERIDO</li>"
#ENVIANDO FOTO DA CNH
def Enviando_CNH(webdriver):
  fieldCNHFieldSend=webdriver.find_element_by_xpath(documentsSendFotos)
  return bool (fieldCNHFieldSend)
wdw.until(Enviando_CNH)
try:
  cnhFoto= driver.find_element_by_xpath(documentsSendFotos)
  cnhFoto.click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO -Não foi possível identificar o campo para envio da CNH\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL IDENTIFICAR O CAMPO PARA ENVIO DA CNH</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Abrindo camera para envio da CNH"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - ABRINDO CAMERA PARA ENVIO DA CNH </li>"

#Acessando a camera para enviar fotos da CNH
############# Configurar IF para utilizar ou não essa função
""" def Selecionando_Camera(webdriver):
  selectingCameraWay=webdriver.find_element_by_id("android:id/button2")
  return bool(selectingCameraWay)
wdw.until(Selecionando_Camera)
try:
  selectCamera= driver.find_element_by_id("android:id/button2")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível encontrar o campo para acessar a camera\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="\nERRO - NÃO FOI POSSÍVEL ENCONTRAR O CAMPO PARA ACESSAR A CAMERA"
else:
    selectCamera.click() """

#BATENDO A FOTO DA CNH
def Batendo_Fotos_CNH(webdriver):
  toTakerPicture=webdriver.find_element_by_xpath(cammeraButton)
  return bool (toTakerPicture)
wdw.until(Batendo_Fotos)
try:
  takeFoto=driver.find_element_by_xpath(cammeraButton).click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel bater nenhuma foto para envio da cnh \n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL BATER NENHUMA FOTO PARA ENVIO DA CNH</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Foto da cnh batida"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - FOTO DA CNH BATIDA</li>"
#ENVIANDO A FOTO DA CNH
def Enviando_Foto_CNH(webdriver):
  toSendPicture = webdriver.find_element_by_xpath(photoConfirm)
  return bool(toSendPicture)
wdw.until(Enviando_Foto_CNH)
try:
  sendFoto=driver.find_element_by_xpath(photoConfirm)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível enviar a foto da cnh\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL ENVIAR A FOTO DA CNH</li>"
  sys.exit()
else:
  sleep(1)
  sendFoto.click()
  sleep(3)
  print(TerminalColor.SUCCESS+"SUCESSO - Foto da cnh enviada"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li> SUCESSO - FOTO DA CNH ENVIADA</li>"
try:
  nextButtonDocuments= driver.find_element_by_xpath(toContinueButtonDocuments)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel prosseguir para a tela de CRLVS\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL PROSSEGUIR PARA A TELA DE CRLVS</li>"
else:
  nextButtonDocuments.click()


#=============================================================================================================================================================
#TELA DE CRLV
#Escrevendo o CRLV no campo de escrita
def Digitando_CRLV(webdriver):
  fieldCRLVFieldSend=webdriver.find_element_by_xpath(toTypeCrlvField)
  return bool (fieldCRLVFieldSend)
wdw.until(Digitando_CRLV)
print('='*40+"\nTela de CRLV")
try:
  sleep(2)
  toTypeCrlv=driver.find_element_by_xpath(toTypeCrlvField).send_keys('Teste fabrica 704')
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível identificar o campo para envio do CRLV\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL IDENTIFICAR O CAMPO PARA ENVIIO DA CRLV</li>"
else:
  sleep(2)
  print(TerminalColor.SUCCESS+"SUCESSO - CRLV inserido"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - CRLV INSERIDO</li>"
#Enviando foto crlv
def Enviando_CRLV(webdriver):
  fieldCNHFieldSend=webdriver.find_element_by_xpath(documentsSendFotos)
  return bool (fieldCNHFieldSend)
wdw.until(Enviando_CRLV)
try:
  cnhFoto= driver.find_element_by_xpath(documentsSendFotos)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível identificar o campo para envio do CRLV\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL IDENTIFICAR O CAMPO PARA ENVIO DO CRLV</li>"
else:
  cnhFoto.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Abrindo camera para envio do CRLV"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - ABRINDO CAMERA PARA ENVIO DO CRLV</li>"

#Acessando a camera para enviar fotos do CRLV
############# Configurar IF para utilizar ou não essa função
""" def Selecionando_Camera_CRLV(webdriver):
  selectingCameraWay = webdriver.find_element_by_id("android:id/button2")
  return bool(selectingCameraWay)
wdw.until(Selecionando_Camera_CRLV)
try:
  selectCamera= driver.find_element_by_id("android:id/button2")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível encontrar o campo para acessar a camera\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="\nERRO - NÃO FOI POSSÍVEL ENCONTRAR O CAMPO PARA ACESSAR A CAMERA"
else:
    selectCamera.click() """

#BATENDO A FOTO DA CRLV
def Batendo_Fotos_CRLV(webdriver):
  toTakerPicture = webdriver.find_element_by_xpath(cammeraButton)
  return bool (toTakerPicture)
wdw.until(Batendo_Fotos_CRLV)
try:
  takeFoto=driver.find_element_by_xpath(cammeraButton)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel bater nenhuma foto para envio do CRLV \n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li> ERRO - NÃO FOI POSSÍVEL BATER NENHUMA FOTO PARA ENVIO DO CRLV</li>"
else:
  sleep(1)
  takeFoto.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Foto da CRLV batida"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - FOTO DA CRLV BATIDA</li>"

#ENVIANDO A FOTO DA CRLV
def Enviando_Foto_CRLV(webdriver):
  toSendPicture = webdriver.find_element_by_xpath(photoConfirm)
  return bool(toSendPicture)
wdw.until(Enviando_Foto_CRLV)
try:
  sendFoto=driver.find_element_by_xpath(photoConfirm)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível enviar a foto do CRLV\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL ENVIAR A FOTO DO CRLV</li>"
  sys.exit()
else:
  sleep(1)
  sendFoto.click()
  sleep(3)
  print(TerminalColor.SUCCESS+"SUCESSO - Foto do CRLV enviada"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - FOTO DO CRLV ENVIADA</li>"
try:
  nextButtonDocuments= driver.find_element_by_xpath(toContinueButtonDocuments)
except:
  print(TerminalColor.ERRO+'='*40+"\nERR0 - Não foi possivel prosseguir para a tela de Antescedentes Criminais\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL PROSSEGUIR PARA A TELA DE ANTESCEDENTES CRIMINAIS</li>"
  sys.exit()
else:
  nextButtonDocuments.click()
  sleep(5)
##################################FIM CRLV




##################################TELA DE ANTESCEDENTES CRIMINAIS########################
#################Escrevendo OS ANTESCENDENTES CRIMINAIS no campo de escrita##############
print('='*40+"\nTela dos Antescedentes Criminais")
def Digitando_AntCrim(webdriver):
  toSendCriminalPast=webdriver.find_element_by_xpath(toTypeCriminalPastField)
  return bool (toSendCriminalPast)
wdw.until(Digitando_AntCrim)
try:
  sleep(1)
  toTypeCriminalPast=driver.find_element_by_xpath(toTypeCriminalPastField)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível identificar o campo para envio dos Antescedentes Criminais\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL IDENTIFICAR O CAMPO PARA ENVIO DE ANTESCEDENTES CRIMINAIS</li>"
else:
  sleep(1)
  toTypeCriminalPast.send_keys('Teste fabrica 704')
  print(TerminalColor.SUCCESS+"SUCESSO - Antescedentes Criminais inseridos"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - ANTESCEDENTES CRIMINAIS INSERIDOS</li>"
#Enviando dos ANTESCEDENTES CRIMINAIS
def Enviando_AntCrim(webdriver):
  fieldToPast=webdriver.find_element_by_xpath(documentsSendFotos)
  return bool (fieldToPast)
wdw.until(Enviando_AntCrim)
try:
  fieldToPast= driver.find_element_by_xpath(documentsSendFotos).click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível identificar o campo para envio dos Antescedentes Criminais\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL IDENTIFICAR O CAMPO PARA ENVIO DOS ANTESCEDENTES CRIMINAIS</li>"
else:
  print(TerminalColor.SUCCESS+"SUCESSO - Abrindo camera para envio dos Antescedentes Criminais"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - ABRINDO CAMERA PARA ENVIO DOS ANTESCEDENTES CRIMINAIS</li>"

#Acessando a camera para enviar fotos dos Antescedentes criminais
#####################ENCONTRAR FORMA DE ESTAR UTILIZANDO IF PARA USAR OU NÃO ESSA
""" def Selecionando_Camera_AntCrim(webdriver):
  selectingCameraWay = webdriver.find_element_by_id("android:id/button2")
  return bool(selectingCameraWay)
wdw.until(Selecionando_Camera_AntCrim)
try:
  selectCamera= driver.find_element_by_id("android:id/button2")
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível encontrar o campo para acessar a camera\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="\nERRO - NÃO FOI POSSÍVEL ENCONTRAR O CAMPO PARA ACESSAR A CAMERA"
else:
    selectCamera.click()
 """
#BATENDO A FOTO DOS ANTESCEDENTES CRIMINAIS
def Batendo_Fotos_AntCrim(webdriver):
  toTakerPicture = webdriver.find_element_by_xpath(cammeraButton)
  return bool (toTakerPicture)
wdw.until(Batendo_Fotos_AntCrim)
try:
  takeFoto=driver.find_element_by_xpath(cammeraButton)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel bater nenhuma foto para envio dos Antescedentes Criminais\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL BATER NENHUMA FOTO PARA ENVIO DAS ANTESCEDENTES CRIMINAIS</li>"
else:
  sleep(1)
  takeFoto.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Foto dos Antescedentes Criminais batida"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - FOTO DOS ANTESCEDENTES CRIMINAIS BATIDA</li>"

#ENVIANDO A FOTO DOS ANTESCEDENTES CRIMINAIS
def Enviando_Foto_AntCrim(webdriver):
  toSendPicture = webdriver.find_element_by_xpath(photoConfirm)
  return bool(toSendPicture)
wdw.until(Enviando_Foto_AntCrim)
try:
  sendFoto=driver.find_element_by_xpath(photoConfirm)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível enviar a foto dos Antescedentes Criminais\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL ENVIAR A FOTO DOS ANTESCEDENTES CRIMINAIS</li>"
  sys.exit()
else:
  sleep(1)
  sendFoto.click()
  sleep(3)
  print(TerminalColor.SUCCESS+"SUCESSO - Foto dos Antescedentes enviada"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - FOTO DOS ANTESCEDENTES ENVIADA</li>"
try:
  nextButtonDocuments= driver.find_element_by_xpath(toContinueButtonDocuments)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel prosseguir para a tela de comprovante de endereço\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL PROSSEGUIR PARA A TELA DE COMPROVANTE DE ENDEREÇO</li>"
  sys.exit()
else:
  nextButtonDocuments.click()
  sleep(5)
#FIM DO CAMPO DE ANTESCEDENTES CRIMINAIS
#=======================================================================================


#CAMPO DE COMPROVANTE DE ENDEREÇO
def Comprovante_de_Endreço(webdriver):
  proofOfAddressField = webdriver.find_element_by_xpath(proofOfAddress)
  return bool (proofOfAddressField)
wdw.until(Comprovante_de_Endreço)
print('='*40+"\nTela para envio do Comprovante de Endereço")
try:
  clickProofOfAddress=driver.find_element_by_xpath(proofOfAddress).click()
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Campo para enviar Comprovante de Endereço não foi encontrado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI ENCONTRADO O CAMPO PARA ENVIO DE COMPROVANTE DE ENDREÇO</li>"
#CAPTURANDO FOTO DO COMPROVANTE DE ENDEREÇO
#####################ENCONTRAR FORMA DE ESTAR UTILIZANDO IF PARA USAR OU NÃO ESSA
""" def Selecionando_Camera_Comprovante(webdriver):
  selectingCameraWay = webdriver.find_element_by_id("android:id/button2")
  return bool(selectingCameraWay)
wdw.until(Selecionando_Camera_Comprovante)
try:
  selectCamera= driver.find_element_by_id("android:id/button2")
  sleep(1)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível encontrar o campo para acessar a camera\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="\nERRO - NÃO FOI POSSÍVEL ENCONTRAR O CAMPO PARA ACESSAR A CAMERA"
else:
  selectCamera.click()
  sleep(1)
  print(TerminalColor.SUCCESS+"SUCESSO -Abrindo camera para envio do Comprovante de Endereço"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="\nSUCESSO - ABRINDO CAMERA PARA ENVIO DO COMPROVANTE DE ENDEREÇO"

 """#BATENDO A FOTO DO COMPROVANTE DE ENDEREÇO
def Batendo_Fotos_Comp(webdriver):
  toTakerPicture = webdriver.find_element_by_xpath(cammeraButton)
  return bool (toTakerPicture)
wdw.until(Batendo_Fotos_Comp)
try:
  takeFoto=driver.find_element_by_xpath(cammeraButton)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel bater nenhuma foto para envio do Comprovante de endereço\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL BATER NENHUMA FOTO PARA ENVIO DO COMPROVANTE DE ENDEREÇO</li>"
else:
  sleep(1)
  takeFoto.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Foto do Comprovante de endereço batida"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - FOTO DO COMPROVANTE DE ENDEREÇO BATIDA</li>"
#ENVIANDO A FOTO DO COMPROVANTE DE ENDEREÇO
def Enviando_Foto_Comp(webdriver):
  toSendPicture = webdriver.find_element_by_xpath(photoConfirm)
  return bool(toSendPicture)
wdw.until(Enviando_Foto_Comp)
try:
  sendFoto=driver.find_element_by_xpath(photoConfirm)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possível enviar a foto do Comprovante de endereço\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL ENVIAR A FOTO DO COMPROVANTE DE ENDEREÇO</li>"
  sys.exit()
else:
  sleep(2)
  sendFoto.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Foto do Comprovante de endereço enviada"+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - FOTO DO COMPROVANTE DE ENDEREÇO ENVIADA</li>"
  sleep(2)
#PASSANDO PARA A ULTIMA TELA
try:
  nextButtonDocuments= driver.find_element_by_xpath(toContinueButtonDocuments)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi possivel prosseguir para a tela de tela de conclusão de cadastro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI POSSÍVEL PROSSEGUIR PARA TELA DE CONCLUSÃO DE CADASTRO</li>"
  sys.exit()
else:
  nextButtonDocuments.click()
  sleep(10)
def Concluindo_Cadastro(webdriver):
  finalButton=webdriver.find_element_by_xpath(lastNextButton)
  return bool (finalButton)
wdw.until(Concluindo_Cadastro)
try:
  clickfinalButton=driver.find_element_by_xpath(lastNextButton)
except:
  print(TerminalColor.ERRO+'='*40+"\nERRO - Não foi encontrado o botão conclusão de cadastro\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>ERRO - NÃO FOI ENCONTRADO O BOTÃO CONCLUSÃO DE CADASTRO</li>"
else:
  clickfinalButton.click()
  print(TerminalColor.SUCCESS+"SUCESSO - Cadastro Finalizado\n"+'='*40+TerminalColor.NORMAL)
  Relatorio_Cadastro_Motorista+="<li>SUCESSO - CADASTRO FINALIZADO</li>"
#FIM

#################################GERANDO RELATORIO#######################################
if os.path.isdir("C:/Users/pedro/Documents/testemobile/Relatorios/"+x): # vemos de este diretorio ja existe
    print ('Ja existe uma pasta com esse nome!')
else:
    os.mkdir("C:/Users/pedro/Documents/testemobile/Relatorios/"+x+" "+data+" "+hora) # aqui criamos a pasta caso nao exista
    with open("C:/Users/pedro/Documents/testemobile/Relatorios/"+x+" "+data+" "+hora+"/TESTE_DE_CADASTRO.html", 'w') as arquivo:
        arquivo.write("Teste realizado\n"+data+"\n")
        arquivo.write(htmlHead+Relatorio_Cadastro_Motorista+htmlFoot)
        print ('Pasta criada com sucesso!')
##################################SCRIPT FINALIZADO######################################