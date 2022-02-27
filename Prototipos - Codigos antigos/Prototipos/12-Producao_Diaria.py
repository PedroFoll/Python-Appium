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
from variaveisProducaodiaria import*
from functions import*
import sys

#Abrindo a produção diaria do motorista e verificando os retornos
try:
    clickDailyProduction = driver.find_element_by_xpath(openDailyProduction)
    clickDailyProduction.click()
except:
    print("Nao foi encontrado o caminho para a producao diaria")
    sys.exit()
else:
    print("Tudo certo, a producao foi aberta")
    sleep(1)


try:
    findProduction = driver.find_element_by_xpath(fieldOfDailyProduction)
except:
    print("Não foi possivel identificar o campo de produção diaria")
    sys.exit()
else:
    print("Campo de produção diaria identificado")
    sleep(1)


#Capturando e mostrando os valores da produção diaria
try:
    findDailyProduction = driver.find_element_by_xpath(dailyValueProduction)
except:
    print("Não foi possivel coletar a producao diaria desse motorista")
    sys.exit()
else:
    print("Foi identificado e a produção diaria foi de: (Valor da producação)")
    sleep(2)

actions = TouchAction(driver)
actions.press(x=911, y=918)
actions.move_to(x=279, y=929) 
actions.release() 
actions.perform()
sleep(1)

#Capturando e mostrando os valores da produção diaria
try:
    findWeeklyProduction = driver.find_element_by_xpath(fieldOfWeeklyProduction)
except:
    print("Não foi possivel coletar a producao semanal desse motorista")
    sys.exit()
else:
    print("Foi identificado, e a produção semanal foi de: (Valor da produção= weeklyValueProduction)")

#Fim