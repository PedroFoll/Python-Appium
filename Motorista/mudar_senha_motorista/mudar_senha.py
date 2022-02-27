from appium.webdriver import Remote
import sys
from time import sleep
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.teste_login.variaveisCadastro import*
from Motorista.teste_login.variaveisProfileMenu import*
from helpers.helpers import Helpers
from Motorista.teste_login.testes_loginM import Teste_Login
from appium.webdriver.common.touch_action import TouchAction


class Trocando_senha:

    
    def troca_senha(dados):
        
        
        executandologin = Teste_Login.Logando_Motorista(dados)
        driver = executandologin['driver']
        driver.implicitly_wait(5)

        localizando = Trocando_senha.localizando_elemento(driver, dados)
        if localizando:
            print("Botão start encontrado")
            Trocando_senha.selecionando_Menu(driver, dados)
            Trocando_senha.selecionando_Perfil(driver, dados)
            Trocando_senha.clickando_Editar_Perfil(driver, dados)
            Trocando_senha.preenchendo_Troca_Senha(driver, dados)
            
            return {'mensagem': 'Deu certo', 'sucesso': True}
    
    def localizando_elemento (driver, dados):

        try:

            driver.find_element_by_xpath(botaoStart)
            return True
        except Exception as erro:
            print(erro)
            textRelatorio = "<li> ERRO Ao clickar em login - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'botão de login não encontrado', 'falhou': False}, erro, sys.exit()
        
    def selecionando_Menu(driver, dados):
        try:

            TouchAction(driver).tap(x=970, y=206).perform()
        except Exception as erro:
            print(erro)
            textRelatorio = '<li>ERRO - ao selecionar menu - FALHOU</li>'
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'mensagem': 'ERRO - ao selecionar menu - FALHOU', 'falhou': False}, erro, sys.exit()

    def selecionando_Perfil(driver, dados):
        try:
            
            sleep(5)
            driver.find_element_by_xpath(profileButton).click()
        except Exception as erro:
            print(erro)
            textRelatorio = '<li>ERRO - ao acessar Perfil - FALHOU</li>'
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'mensagem': 'ERRO - ao acessar Perfil - FALHOU', 'falhou': False}, erro, sys.exit()

    def clickando_Editar_Perfil(driver, dados):
        try:

            sleep(5)
            driver.find_element_by_xpath(editProfileButton).click()
            sleep(10)
        except Exception as erro:
            textRelatorio = '<li>ERRO - ao tentar editar o Perfil - FALHOU</li>'
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'mensagem': 'ERRO - ao tentar editar o Perfil - FALHOU', 'falhou': False}, erro, sys.exit()
    
    def preenchendo_Troca_Senha(driver, dados):
        try:
            
            driver.find_element_by_xpath(currentPassword)
            if currentPassword:
                driver.find_element_by_xpath(currentPassword).send_keys('123456')
                

        except Exception as erro:
            print(erro)
            textRelatorio = '<li>ERRO - ao tentar editar o Perfil - FALHOU</li>'
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'mensagem': 'ERRO - ao tentar editar o Perfil - FALHOU', 'falhou': False}, erro, sys.exit()

        try:
            
            driver.find_element_by_xpath(newPassword)
            if newPassword:
                driver.find_element_by_xpath(newPassword).send_keys('123456')
                

        except Exception as erro:
            print(erro)
            textRelatorio = '<li>ERRO - ao tentar editar o Perfil - FALHOU</li>'
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'mensagem': 'ERRO - ao tentar editar o Perfil - FALHOU', 'falhou': False}, erro, sys.exit()

        try:
            driver.find_element_by_xpath(confirmationPassword)
            if confirmationPassword:
                driver.find_element_by_xpath(confirmationPassword).send_keys('123456')
                

        except Exception as erro:
            print(erro)
            textRelatorio = '<li>ERRO - ao tentar editar o Perfil - FALHOU</li>'
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'mensagem': 'ERRO - ao tentar editar o Perfil - FALHOU', 'falhou': False}, erro, sys.exit()

        else:
            driver.find_element_by_xpath(savePassword).click()
            textRelatorio = '<li>Sucesso- Senha alterada</li>'
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            print("Deu certo boy")