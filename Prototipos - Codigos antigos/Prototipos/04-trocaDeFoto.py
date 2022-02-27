from ast import Break, If
from inspect import _void
from socket import timeout
from variaveisProfileMenu import*
from operator import ne
import random
from sys import platform
import random
from tracemalloc import stop
import unittest
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
clicklogin1 = driver.find_element_by_xpath(botaoLoginM)
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
sleep(30)

#Começando a troca de foto
actions=TouchAction(driver).tap(x=970, y=206).perform()
sleep(6)
profileClick=driver.find_element_by_xpath(profileButton)
profileClick.click()
sleep(2)
editProfileClick=driver.find_element_by_xpath(editProfileButton)
editProfileClick.click()
sleep(2)
changeFoto=driver.find_element_by_xpath(editImage)
changeFoto.click()
sleep(3)
takeFoto=driver.find_element_by_accessibility_id("Shutter")
takeFoto.click()
sleep(4)
sendFoto= driver.find_element_by_accessibility_id("Done")
sendFoto.click()
sleep(3)

#final