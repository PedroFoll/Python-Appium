from ast import Break, If
from inspect import _void
from variaveisProfileMenu import*
from operator import ne
from sys import platform
from tracemalloc import stop
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
 # "appium:app": "C:/Users/pedro/Documents/testemobile/app-test.apk"
})
#Login
""" clicklogin1 = driver.find_element_by_xpath(botaoLoginM)
clicklogin1.click()
sleep(6)

#email
emailM = driver.find_element_by_xpath(campoEmailM)
emailM.send_keys("motorista@teste.com")
#senha
clicksenha1= driver.find_element_by_xpath(campoSenhaM)
clicksenha1.send_keys("654321")
sleep(3)

botaoLogin=driver.find_element_by_xpath (botaoLoginM2)
botaoLogin.click()
sleep(30) """

#Começando a troca de foto
""" actions=TouchAction(driver).tap(x=970, y=206).perform()
sleep(6) """
""" saldoMotorista=driver.find_element_by_xpath(balanceDriver)
saldoMotorista.

print(saldoMotorista) """

#Vai ficar pra depois