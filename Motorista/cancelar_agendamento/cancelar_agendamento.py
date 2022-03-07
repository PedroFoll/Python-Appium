import sys
from time import sleep
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.teste_login.variaveisCadastro import*
from Motorista.teste_login.variaveisProfileMenu import*
from Motorista.teste_login.variaveisAceitandoCorridas import*
from helpers.helpers import Helpers
from Motorista.teste_login.testes_loginM import Teste_Login
from appium.webdriver.common.touch_action import TouchAction
from Motorista.aceitar_corrida_agendada.aceitando_corrida_agendada import Aceitar_Agendamento

class Cancelar_agendamento:
    
    
    def cancelando_corrida_agendada(dados):
        
        
        aceitandoagendamento = Aceitar_Agendamento.aceitando_corrida(dados)
        driver = aceitandoagendamento['driver']
        driver.implicitly_wait(20)

        localizando = Cancelar_agendamento.acessando_tela_de_agendamentos_aceitos(driver, dados)
        if localizando:
            
            Cancelar_agendamento.selecionando_corrida_aceitada(driver, dados)
            Cancelar_agendamento.confirmando_cancelamento(driver, dados)

            return Cancelar_agendamento.aceitando_confirmação_de_cancelamento(driver,dados)    

   
    def acessando_tela_de_agendamentos_aceitos(driver, dados):
        try:
            driver.find_element_by_xpath(aceptedTrips)
            if aceptedTrips:
                driver.find_element_by_xpath(aceptedTrips).click()
                return True

        except:
            textRelatorio = "<li> Aviso - Não foi solicitado nenhuma corrida agendada recentemente - Aviso - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Não foi solicitado nenhuma corrida agendada recentemente', 'falhou': False}, quit()

    def selecionando_corrida_aceitada(driver, dados):
        try:
        
            driver.find_element_by_xpath(cancelTheTrip)
            if cancelTheTrip:
                driver.find_element_by_xpath(cancelTheTrip).click()
        except:
            textRelatorio = "<li> Aviso - Nenhuma agendamento foi aceito por esse motorista - Aviso - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Nenhuma agendamento foi aceito por esse motorista', 'falhou': False}, quit()

    def confirmando_cancelamento(driver, dados):
        try:
        
            driver.find_element_by_xpath(yesAcceptOrCancelTrip)
            if yesAcceptOrCancelTrip:
                driver.find_element_by_xpath(yesAcceptOrCancelTrip).click()
        except:
            textRelatorio = "<li> Aviso - Botao para cancelamneto da corrida agendada nao foi encontrado - Aviso - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Botao para cancelamneto da corrida agendada nao foi encontrado', 'falhou': False}, quit()

    def aceitando_confirmação_de_cancelamento(driver, dados):
        try:

            driver.find_element_by_xpath(afterAcceptedOrCancelTrip)
            if afterAcceptedOrCancelTrip:
                driver.find_element_by_xpath(afterAcceptedOrCancelTrip).click()
                textRelatorio = "<li> Corrida agendada foi cancelada com sucesso</li>"
                GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                return {'Mensagem': 'Corrida agendada foi cancelada com sucesso', 'sucesso': True}


        except:
            textRelatorio = "<li> Aviso - Campo da confirmacao da confirmacao de cancelamento nao foi identificado - Aviso - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Campo da confirmacao da confirmacao de cancelamento nao foi identificado', 'falhou': False}, quit()
