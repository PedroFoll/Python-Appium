from ast import Break, If, Try
from inspect import _void
from lib2to3.pgen2.driver import Driver
from select import select
from variaveisAceitandoCorridas import*
from variaveisProfileMenu import*
from variaveisbotaoemergencia import*
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

#Click para abrir a aba de segurança
""" try:
    clickSecurityButton = driver.find_element_by_xpath(securityButton)
    clickSecurityButton.click()
except:
    print("Não foi possivel dar duplo click no botão")
    sys.exit()
else:
    print("Duplo click realizado")
    sleep(3) """
#O Codigo a cima não está funcionando, porém, temos que buscar uma forma de dar duplo click

#Buscando Botões de denuncia
#Botão de racismo

try:
    findRacismButton = driver.find_element_by_xpath(racismHarassmentEmbarrassment)
except:
    print("Botão de denuncia por racismo não encontrado")
else:
    print("Botão de racismo encontrado")
#Botão de acidente
try:
    findAccidentButton = driver.find_element_by_xpath(personalAccidentVehicle)
except:
    print("Botão de denuncia por acidente pessoal ou veicular ")
else:
    print("Botão de acidente pessoal ou veicular encontrado")
#botão de mudança de rota
try:
    findChangeRouteButton = driver.find_element_by_xpath(changeOfRoute)
except:
    print("Botão de denuncia por troca de rota não encontrado")
else:
    print("Botão de troca de rota encontrado")
#Botão de Assalto e Sequestro
try:
    findRobberyOrKidnapButton = driver.find_element_by_xpath(RobberyOrKidnapping)
except:
    print("Botão de denuncia por assalto ou sequestro")
else:
    print("Botão de assalto ou sequestro encontrado")
#Botão de divergencia de valores
try:
    findDivergenceButton = driver.find_element_by_xpath(DivergenceOfValues)
except:
    print("Botão de denuncia por divergencia de valores não encontrado")
else:
    print("Botão de divergencia de valores encontrado")

sys.exit()
#O click em qualquer botão não apresente comportamento especifico, a certificação é enviada ao monitor.

#fim