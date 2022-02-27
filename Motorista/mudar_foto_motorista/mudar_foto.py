from appium.webdriver import Remote
import sys
from time import sleep
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.teste_login.variaveisCadastro import*
from Motorista.teste_login.variaveisProfileMenu import*
from helpers.helpers import Helpers
from Motorista.teste_login.testes_loginM import Teste_Login
from appium.webdriver.common.touch_action import TouchAction


class Mudar_Foto:

    
    def mudando_foto(dados):
        
        
        executandologin = Teste_Login.Logando_Motorista(dados)
        driver = executandologin['driver']
        driver.implicitly_wait(5)

        localizando = Mudar_Foto.localizando_elemento(driver, dados)
        if localizando:

            print("Botão start encontrado")
            Mudar_Foto.selecionando_Menu(driver, dados)
            Mudar_Foto.selecionando_Perfil(driver, dados)
            Mudar_Foto.clickando_Editar_Perfil(driver, dados)
            Mudar_Foto.enviando_nova_foto(driver, dados)

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
            

    def enviando_nova_foto(driver,dados):
        try:

            print("oi")
            driver.find_element_by_xpath(butonChangePhoto)
            if butonChangePhoto:
                driver.find_element_by_xpath(butonChangePhoto).click()
                sleep(5)
                try:

                    driver.find_element_by_xpath(allowUseMidia)
                    if allowUseMidia:
                        driver.find_element_by_xpath(allowUseMidia).click()
                        sleep(5)
                        
                except :
                    print(" erro ao tentar permitir o uso de midia")
                    textRelatorio = '<li>Permissao ao uso de midia ja concedido</li>'
                    GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'mensagem': 'Permissao ao uso de midia ja concedido', 'falhou': False}
            
            try:

                driver.find_element_by_xpath(cammeraButton)
                sleep(3)
                if cammeraButton:
                    driver.find_element_by_xpath(cammeraButton).click()
                    sleep(3)
                else:
                    textRelatorio = "<li> ERRO NÃO FOI POSSIVEL  BATER A FOTO - FALHOU</li>"
                    GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'NÃO FOI POSSIVEL  BATER A FOTO', 'falhou': False}, erro, sys.exit()

            except Exception as erro:
                textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA BATER A FOTO - FALHOU</li>"
                GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA BATER A FOTO', 'falhou': False}, erro, sys.exit()

            else:
                sleep(5)


            try:

                driver.find_element_by_xpath(photoConfirm)
                sleep(3)
                if photoConfirm:
                        driver.find_element_by_xpath(photoConfirm).click()
                        sleep(3)
                else:
                    textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENVIAR A FOTO - FALHOU</li>"
                    GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'NÃO FOI POSSIVEL ENVIAR A FOTO', 'falhou': False}, erro, sys.exit()

            except Exception as erro:
                textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA ENVIO - FALHOU</li>"
                GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA ENVIO', 'falhou': False}, erro, sys.exit()
            
            try:
                driver.find_element_by_xpath(confirmPictureSend)
                if confirmPictureSend:
                    driver.find_element_by_xpath(confirmPictureSend).click()
            except:
                textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENVIAR FOTO  - FALHOU</li>"
                GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                return {'Mensagem': 'NÃO FOI POSSIVEL ENVIAR FOTO ', 'falhou': False}, erro, sys.exit()




        except:
            textRelatorio = "<li> ERRO NÃO FOI ENCONTRADO CAMPO PARA MUDANÇA DE FOTO - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI ENCONTRADO CAMPO PARA MUDANÇA DE FOTO', 'falhou': False}, erro, sys.exit()

        else:
            textRelatorio = "<li>SUCESSO - SOLICITAÇÃO DE TROCA DE FOTO ENVIADA </li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'SUCESSO - SOLICITAÇÃO DE TROCA DE FOTO ENVIADA', 'falhou': False}