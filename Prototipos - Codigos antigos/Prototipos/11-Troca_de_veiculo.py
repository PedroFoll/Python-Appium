from ast import Break, If, Try
from inspect import _void
from lib2to3.pgen2.driver import Driver
from select import select
from variaveisAceitandoCorridas import*
from variaveisProfileMenu import*
from sys import platform
import random
from time import sleep
from appium.webdriver import Remote
from appium.webdriver.extensions.search_context import android
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

#Abrindo e escrevendo no arquivo html os procedimentos que iremos realizar nesse codigo.
f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
f1.write("\n<h3> Testes de alteracao de veiculos do motorista </h3>\n<hr>")
driver= Remote( 
        'http://localhost:4723/wd/hub',
{
  "platformName": "android",
  "appium:deviceName": "AppiumP",
  "appium:avd": "Pixel_5_API_29",
#   "appium:app": "C:/Users/pedro/Documents/Projetos Python-Appium/app-test.apk"
}
)
#Definindo variavel para esperas
"""
try:
    clicklogin1 = driver.find_element_by_xpath(botaoLoginM).click()
except:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("Nao foi possivel comecar o login no aplicativo de motoirsta")
    print("Nao foi localizado o elemento botaoLoginM")
sleep(6)
 """
"""#email
emailM = driver.find_element_by_xpath(campoEmailM)
emailM.send_keys("motorista@teste.com")
#senha
clicksenha1= driver.find_element_by_xpath(campoSenhaM)
clicksenha1.send_keys("123456")
sleep(6)

#Apertando no botão logar
try:
    botaoLogin=driver.find_element_by_xpath (botaoLoginM2)
    botaoLogin.click()
except:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("Não foi possivel realizar o login")
    print("Nao foi localizado o elemento: botaoLoginM2")
else:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("Login realizado com sucesso")
sleep(20)
 """
#Ficando online
""" try:
    clickStarting = driver.find_element_by_xpath(startButton)
    clickStarting.click()
except:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("/n<br>Nao foi possivel ficar online<br>")
    print("Nao foi localizado o elemento: startButton")
sleep(20) """
 
#Entrando no menu
actions=TouchAction(driver).tap(x=970, y=206).perform()
sleep(6)
try:
    profileClick=driver.find_element_by_xpath(profileButton)
    profileClick.click()
except:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("Campo de perfil nao encontrado")
    print("Campo de perfil nao encontrado")
sleep(3)

#Encontrando os botões e enviando os dados do novo carro.
try:
    vehiclesField = driver.find_element_by_xpath(vehiclesButton)
    vehiclesField.click()
except:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("Campo de vizualisação do veiculo nao foi encontrado")
    print("Campo de vizualisação do veiculo nao foi encontrado")
else:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("Campo de vizualisação do veiculo foi acessado")
    print("Campo de vizualisação do veiculo foi acessado")
sleep(6)

try:
    clickRequestChangeVehicles = driver.find_element_by_xpath(requestChangeVehicle)
    clickRequestChangeVehicles.click()
except:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("Campo de enviar os dados do novo veiculo não foi encontrado")
    print("Campo de enviar os dados do novo veiculo não foi encontrado")
else:
    f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/Fabrica Homologacao",'at')
    f1.write("Campo de enviar os dados do novo veiculo foi encontrado")
    print("Campo de enviar os dados do novo veiculo foi encontrado")
""" driver.implicitly_wait(10)
 """
sleep(6)
#Dados do novo veiculo
toTypeNewBrand = driver.find_element_by_xpath(newBrand)
toTypeNewBrand.send_keys("Chevrolet")
toTypeNewModel = driver.find_element_by_xpath(newModel)
toTypeNewModel.send_keys("Onix")
toTypeNewPlate = driver.find_element_by_xpath(newPlate)
toTypeNewPlate.send_keys('TST-0704')
toTypeNewVinNumber = driver.find_element_by_xpath(newRenavam)
toTypeNewVinNumber.send_keys('12171174856') #Não sei a formatação do renavam
toTypeNewColor = driver.find_element_by_xpath(newColor)
toTypeNewColor.send_keys('Cinza')
toTypeNewVehicleYear = driver.find_element_by_xpath(newCarYear)
toTypeNewVehicleYear.send_keys('2016')
toSendRequest = driver.find_element_by_xpath(sendButton)
toSendRequest.click()
sleep(2)
clickOkEnd = driver.find_element_by_xpath(okFinalCarChange)
clickOkEnd.click()

#Fim