import sys
from time import sleep
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.teste_login.variaveisCadastro import*
from Motorista.teste_login.variaveisProfileMenu import*
from Motorista.teste_login.variaveisAceitandoCorridas import*
from helpers.helpers import Helpers
from Motorista.teste_login.testes_loginM import Teste_Login
from appium.webdriver.common.touch_action import TouchAction


class Aceitar_Agendamento:

    
    def aceitando_corrida(dados):
        
        
        executandologin = Teste_Login.Logando_Motorista(dados)
        driver = executandologin['driver']
        driver.implicitly_wait(20)

        localizando = Aceitar_Agendamento.localizando_elemento(driver, dados)
        if localizando:
            
            Aceitar_Agendamento.sobrepondo_apps(driver, dados)
            Aceitar_Agendamento.Acessar_tela_viagem_Agendada(driver, dados)
            Aceitar_Agendamento.selecionando_corrida(driver, dados)
            Aceitar_Agendamento.confirmando_corrida_agendada(driver, dados)
            Aceitar_Agendamento.confirmação_final_aceitando_corrida(driver, dados)

            return {'mensagem': 'Deu certo', 'sucesso': True}
    
    def localizando_elemento (driver, dados):

        try:

            driver.find_element_by_xpath(botaoStart)
        except Exception as erro:
            print(erro)
            textRelatorio = "<li> ERRO Ao clickar em login - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'botão de login não encontrado', 'falhou': False}, quit()

        else:
            driver.find_element_by_xpath(botaoStart).click()
            return True

    def sobrepondo_apps(driver, dados):
        try:

            driver.find_element_by_xpath(overOtherApps)
            if overOtherApps:
                driver.find_element_by_xpath(overOtherApps).click()
                sleep(5)
                driver.back()

        except:
            textRelatorio = "<li>SUCESSO - PERMISSAO PARA SOBREPOR APLICATIVOS JA ESTAVA ATIVA </li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'PERMISSAO PARA SOBREPOR APLICATIVOS JA ESTAVA ATIVA', 'sucesso': True}
    
    def Acessar_tela_viagem_Agendada(driver, dados):
        try:

            driver.find_element_by_xpath(scheduleTrip)
            if scheduleTrip:
                driver.find_element_by_xpath(scheduleTrip).click()
                                
        except:
            print("Não existe corrida agendada")
            textRelatorio = "<li> ERRO - NÃO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO- FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO', 'falhou': False}, quit()

    def selecionando_corrida(driver, dados):
        try:

            driver.find_element_by_xpath(acceptTheTrip)
            if acceptTheTrip:
                driver.find_element_by_xpath(acceptTheTrip).click()

        except:
            print("Não existe corrida agendada")
            textRelatorio = "<li> ERRO - NÃO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO- FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO', 'falhou': False}, quit()

    def confirmando_corrida_agendada(driver, dados):

        try:
            
            driver.find_element_by_xpath(yesAcceptOrCancelTrip)
            if yesAcceptOrCancelTrip:
                driver.find_element_by_xpath(yesAcceptOrCancelTrip).click()
        
        except:
            textRelatorio = "<li> ERRO - NÃO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO- FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO', 'falhou': False}, quit()
        
    def confirmação_final_aceitando_corrida(driver, dados):

        try:

            driver.find_element_by_xpath(afterAcceptedOrCancelTrip)
            if afterAcceptedOrCancelTrip:
                driver.find_element_by_xpath(afterAcceptedOrCancelTrip).click()
        
        except:
            textRelatorio = "<li> ERRO - NÃO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO- FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO', 'falhou': False}, quit()