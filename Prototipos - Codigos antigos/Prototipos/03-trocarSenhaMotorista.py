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

#Entrando no menu e trocando senha
actions=TouchAction(driver).tap(x=970, y=206).perform()
sleep(6)
profileClick=driver.find_element_by_xpath(profileButton)
profileClick.click()
sleep(2)
editProfileClick=driver.find_element_by_xpath(editProfileButton)
editProfileClick.click()
sleep(2)
changePasswordcurrent=driver.find_element_by_xpath(currentPassword)
changePasswordcurrent.send_keys('123456')
changePasswordnew=driver.find_element_by_xpath(newPassword)
changePasswordnew.send_keys('654321')
changePasswordconfirm=driver.find_element_by_xpath(confirmationPassword)
changePasswordconfirm.send_keys('654321')
sleep(2)
clickSavePassword=driver.find_element_by_xpath(savePassword)
clickSavePassword.click()

#Fim da troca de senha