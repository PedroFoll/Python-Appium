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
 
#Entrando no menu
actions=TouchAction(driver).tap(x=970, y=206).perform()
sleep(6)
profileClick=driver.find_element_by_xpath(profileButton)
profileClick.click()
sleep(2)

#Clickando no Reportar informações
clickReport = driver.find_element_by_xpath(reportInformationAppButton)
clickReport.click()
clickInformationSent = driver.find_element_by_xpath(okInformationSent)
clickInformationSent.click()

#Fim