from ast import Break, If
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
driver= Remote( 
        'http://localhost:4723/wd/hub',
{
  "platformName": "android",
  "appium:deviceName": "AppiumP",
  "appium:avd": "Pixel_5_API_29",
#   "appium:app": "C:/Users/pedro/Documents/Projetos Python-Appium/app-test.apk"
}
)

""" #Login
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
sleep(20)"""

#Aceitando Corrida agendada 
#Ficando online
clickStarting = driver.find_element_by_xpath(startButton)
clickStarting.click()
#Abrindo a listagem de corridas agendadas
clickScheduleTrip = driver.find_element_by_xpath(scheduleTrip)
clickScheduleTrip.click()
clickAcceptTrip = driver.find_element_by_xpath(acceptTheTrip)
clickAcceptTrip.click()
clickYesAcceptTrip = driver.find_element_by_xpath(yesAcceptOrCancelTrip)
clickYesAcceptTrip.click()
clickOkAfterAcceptTrip = driver.find_element_by_xpath(afterAcceptedOrCancelTrip)
clickOkAfterAcceptTrip.click()


#Cancelando a corrida agendada que já foi aceita pelo motorista
clickAcceptedTrips = driver.find_element_by_xpath(aceptedTrips)
clickAcceptedTrips.click()
clickCancelTrip = driver.find_element_by_xpath(cancelTheTrip)
clickCancelTrip.click()
clickYesAcceptTrip = driver.find_element_by_xpath(yesAcceptOrCancelTrip)
clickYesAcceptTrip.click()
clickOkAfterAcceptTrip = driver.find_element_by_xpath(afterAcceptedOrCancelTrip)
clickOkAfterAcceptTrip.click()

#Fim - Funcionando.