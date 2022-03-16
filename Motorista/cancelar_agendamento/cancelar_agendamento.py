import sys
from time import sleep
from Motorista.variaveis.variaveis import*
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
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
                    textRelatorio = 'Não foi aceito nenhuma corrida ou não existem corridas agendadas'
                    GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                    return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 

    def selecionando_corrida_aceitada(driver, dados):
        try:
        
            driver.find_element_by_xpath(cancelTheTrip)
            if cancelTheTrip:
                driver.find_element_by_xpath(cancelTheTrip).click()
        except:
            textRelatorio = 'Nenhuma agendamento foi aceito por esse motorista'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 

    def confirmando_cancelamento(driver, dados):
        try:
        
            driver.find_element_by_xpath(yesAcceptOrCancelTrip)
            if yesAcceptOrCancelTrip:
                driver.find_element_by_xpath(yesAcceptOrCancelTrip).click()
        except:
            textRelatorio = 'Botao para cancelamneto da corrida agendada nao foi encontrado'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 

    def aceitando_confirmação_de_cancelamento(driver, dados):
        try:

            driver.find_element_by_xpath(afterAcceptedOrCancelTrip)
            if afterAcceptedOrCancelTrip:
                
                driver.find_element_by_xpath(afterAcceptedOrCancelTrip).click()
                textRelatorio = 'Corrida agendada foi cancelada com sucesso'
                GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status="Sucesso")
                return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 


        except:
            textRelatorio = 'Campo da confirmacao da confirmacao de cancelamento nao foi identificado'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 
