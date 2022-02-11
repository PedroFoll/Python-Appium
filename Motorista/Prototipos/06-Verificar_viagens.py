from ast import Break, If
from cProfile import label
from inspect import _void
from timeit import repeat
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
  "appium:app": "C:/Users/pedro/Documents/testemobile/app-test.apk"
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

#Entrando no menu
actions=TouchAction(driver).tap(x=970, y=206).perform()
clickMyTrips=driver.find_element_by_xpath(myTripsButton)
clickMyTrips.click()
sleep(3)
clickInTheTrip=driver.find_element_by_xpath(theTrip)
clickInTheTrip.click()
sleep(3)
actions = TouchAction(driver)
actions.press(x=966, y=2139)
actions.move_to(x=946, y=440)
actions.release() 
actions.perform()
sleep(2)
actions = TouchAction(driver)
actions.press(x=966, y=2139)
actions.move_to(x=946, y=440)
actions.release()
actions.perform()
sleep(1)

clickliberationRequest=driver.find_element_by_xpath(liberationRequest)
clickliberationRequest.click()
sleep(2)
toTypeReleaseTripRequest=driver.find_element_by_xpath(describeTrip)
toTypeReleaseTripRequest.send_keys("Teste fabrica704")
sleep(1)
toClickSendReleaseTripRequest=driver.find_element_by_xpath(sendRequestReleaseTrip)
toClickSendReleaseTripRequest.click()
sleep(1)
toClickOk24h=driver.find_element_by_xpath(confirm24hWait)
toClickOk24h.click()

#Fim