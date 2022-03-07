from time import sleep
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.teste_login.variaveisCadastro import*
from Motorista.teste_login.variaveisProfileMenu import*
from Motorista.teste_login.variaveisAceitandoCorridas import*
from Motorista.teste_login.testes_loginM import Teste_Login
from helpers.helpers import Helpers
from os import sys

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
            

            return Aceitar_Agendamento.confirmação_final_aceitando_corrida(driver, dados)
    
    def localizando_elemento (driver, dados):

        try:

            driver.find_element_by_xpath(botaoStart)
        
        except Exception as erro:
            Helpers.conexao_db(dados=dados, Mensagem="Iniciar nao encontrado",nome_relatorio="Teste Aceitando Corrida Agendada",status = "Falhou"), sys.exit()        
        
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
            return "Permissão de sobreposição de consedida"
    def Acessar_tela_viagem_Agendada(driver, dados):
        try:

            driver.find_element_by_xpath(scheduleTrip)
            if scheduleTrip:
                driver.find_element_by_xpath(scheduleTrip).click()
                                
        except:
            Helpers.conexao_db(dados=dados, Mensagem="NAO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO",nome_relatorio="Teste Aceitando Corrida Agendada",status = "Falhou"), sys.exit()        
    def selecionando_corrida(driver, dados):
        try:

            driver.find_element_by_xpath(acceptTheTrip)
            if acceptTheTrip:
                driver.find_element_by_xpath(acceptTheTrip).click()

        except:
            Helpers.conexao_db(dados=dados, Mensagem="NAO EXISTE NENHUMA CORRIDA EM AGENDAMENTOS",nome_relatorio="Teste Aceitando Corrida Agendada",status = "Falhou"), sys.exit()
    def confirmando_corrida_agendada(driver, dados):

        try:
            
            driver.find_element_by_xpath(yesAcceptOrCancelTrip)
            if yesAcceptOrCancelTrip:
                driver.find_element_by_xpath(yesAcceptOrCancelTrip).click()
        
        except:
            Helpers.conexao_db(dados=dados, Mensagem="NAO EXISTE NENHUMA CORRIDA AGENDADA NO MOMENTO",nome_relatorio="Teste Aceitando Corrida Agendada",status = "Falhou"), sys.exit()
    def confirmação_final_aceitando_corrida(driver, dados):

        try:

            driver.find_element_by_xpath(afterAcceptedOrCancelTrip)
            if afterAcceptedOrCancelTrip:
                driver.find_element_by_xpath(afterAcceptedOrCancelTrip).click()
        
        except:
            Helpers.conexao_db(dados=dados, Mensagem="NAO FOI POSSIVEL ACEITAR A CORRIDA AGENDADA",nome_relatorio="Teste Aceitando Corrida Agendada",status = "Falhou"), sys.exit()
        else:
            Helpers.conexao_db(dados=dados, Mensagem="TESTE DE ACEITE DE CORRIDA AGENDADA CONCLUIDO",nome_relatorio="Teste Aceitando Corrida Agendada",status = "Sucesso")
            return {'driver': driver}