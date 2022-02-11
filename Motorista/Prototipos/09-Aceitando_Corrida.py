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
import sys
driver= Remote( 
        'http://localhost:4723/wd/hub',
{
  "platformName": "android",
  "appium:deviceName": "AppiumP",
  "appium:avd": "Pixel_5_API_29",
#   "appium:app": "C:/Users/pedro/Documents/Projetos Python-Appium/app-test.apk"
}
)

#Login
clicklogin1 = driver.find_element_by_xpath(botaoLoginM)
clicklogin1.click()
sleep(6)

#email
emailM = driver.find_element_by_xpath(campoEmailM)
emailM.send_keys("motorista@teste.com")
#senha
clicksenha1= driver.find_element_by_xpath(campoSenhaM)
clicksenha1.send_keys("123456")
sleep(6)

botaoLogin=driver.find_element_by_xpath (botaoLoginM2)
botaoLogin.click()
sleep(20)

#Ficando online
clickStarting = driver.find_element_by_xpath(startButton)
clickStarting.click()
sleep(20)
 
#Aceitando a corrida

try:
    beCallingByClient = driver.find_element_by_xpath(callTrip)
    beCallingByClient.click()
except:
    print("Não temos corridas disponiveis no momento")
else:
    actions = TouchAction(driver)
    actions.press(x=430, y=1823)
    actions.move_to(x=437, y=1166) 
    actions.release() 
    actions.perform()
    sleep(6)


#Sinalizando a chegada ao cliente.
actions = TouchAction(driver)
actions.press(x=144, y=2036) 
actions.move_to(x=798, y=2033) 
actions.release() 
actions.perform()
sleep(6)
#Iniciando a corrida.actions = TouchAction(driver)
actions.press(x=107, y=2036)
actions.move_to(x=839, y=2046)
actions.release() 
actions.perform()
sleep(6) 

#Abrindo chat e enviando uma mensagem
try:
    openChat = driver.find_element_by_xpath(chatBubble)
except:
    print("Não foi possível encontrar o elemento")
    sys.exit()
else:
    print("Elemento do chat encontrado encontrado")
    openChat.click()
sleep(3)
#Enviando uma mensagem e certificando que foi enviada
try:
    sendMsg = driver.find_element_by_xpath(fieldOfText)
except:
    print("Não foi possível abrir o chat com o cliente")
    sys.exit()

else:
    print("O chat foi aberto e estou enviando uma mensagem de testes para passageiro")
    sendMsg.send_keys("Olá, estou realizando um teste de mensagens no seu aplicativo")
    sleep(2)
    clickSendMsg =driver.find_element_by_xpath(toSendTheMsg)
    clickSendMsg.click()

try:
    ifMsgWasSent = driver.find_element_by_xpath(theSentMsg)
except:
    print("A Mensagem não pôde ser enviada")
    sys.exit()
else:
    print("A Mensagem foi enviada com sucesso")
sleep(2)
try:
    backButton = driver.find_element_by_xpath(toBackButton)
except:
    print("Não está aparecendo o botão de voltar")
    sys.exit()
else:
    print("Botão de voltar disponivel, estarei voltando para a tela da viagem")
    backButton.click()


#Finalizando a corrida
try:
    finishTheTrip = driver.find_element_by_xpath(slideButton)
except:
    print("Campo para finalizar corrida não foi encontrado")
    sys.exit
else:
    print("Agora que todos os processos foram finalizados, estaremos finalizando a corrida também")
    actions.press(x=110, y=2036)
    actions.move_to(x=770, y=2036)
    actions.release() 
    actions.perform()
    sleep(15)
try:
    clickCloseButton = driver.find_element_by_xpath(closeResumTrip)
except:
    print("Não foi encontrada o botão de fechar o resumo da corrida")
else:
    closeResumTrip.click()
print("Finalizando a automação do teste de corrida")

sys.exit()
#fim