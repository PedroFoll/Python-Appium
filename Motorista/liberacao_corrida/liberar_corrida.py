import sys
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.teste_login.acoes_na_tela import*
from Motorista.variaveis.variaveis import*
from Motorista.teste_login.testes_loginM import Teste_Login
from appium.webdriver.common.touch_action import TouchAction

class Liberar_corrida():
    
    def liberando_corrida(dados):
        
        
        executandologin = Teste_Login.Logando_Motorista(dados)
        driver = executandologin['driver']
        driver.implicitly_wait(20)

        localizando = Liberar_corrida.localizando_elemento(driver, dados)
        if localizando:
            
            print("encontrando botao start")
            Liberar_corrida.acessando_menu(driver, dados)
            Liberar_corrida.acessando_viagens(driver,dados)
            Liberar_corrida.selecionando_viagem(driver,dados)
            Liberar_corrida.solicitando_liberacao(driver, dados)
            Liberar_corrida.digitando_requisicao(driver,dados)
            Liberar_corrida.confirmar_envio(driver,dados)
            

            return Liberar_corrida.confirmar_espera(driver,dados)


    def localizando_elemento(driver,dados):
        try:
            
            driver.find_element_by_xpath(botaoStart)
            return True
        except Exception as erro:
            print(erro)
            textRelatorio = "Botão para ficar online não necontrando"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 

    def acessando_menu(driver, dados):
        try:
            
            TouchAction(driver).tap(x=970, y=206).perform()
        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao selecionar menu"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao selecionar menu', 'falhou': False},sys.exit() 
        
    def acessando_viagens(driver,dados):
        try:
            
            driver.find_element_by_xpath(myTripsButton)
            if myTripsButton:
                driver.find_element_by_xpath(myTripsButton).click()


        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao selecionar menu de viagens"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao selecionar menu de viagens', 'falhou': False},sys.exit() 
        
    def selecionando_viagem(driver,dados):
        try:
        
            driver.find_element_by_xpath(theTrip)
            if theTrip:
                driver.find_element_by_xpath(theTrip).click()
        
        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao selecionar menu de viagens"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao selecionar menu de viagens', 'falhou': False},sys.exit() 
        
    def solicitando_liberacao(driver,dados):
        try:

            Mover_tela.movendo_para_baixo(driver)
            driver.find_element_by_xpath(liberationRequest)
            if liberationRequest:
                driver.find_element_by_xpath(liberationRequest).click()

        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao selecionar viagem a ser liberada"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao selecionar viagem a ser liberada', 'falhou': False},sys.exit() 
    
    def digitando_requisicao(driver, dados):
        try:

            driver.find_element_by_xpath(describeTrip)
            if describeTrip:
                driver.find_element_by_xpath(describeTrip).send_keys("Teste fabrica704")
        except Exception as erro:
            textRelatorio = "Não foi possível inserir o motivo da requisição de liberação"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Não foi possível inserir o motivo da requisição de liberação', 'falhou': False},sys.exit() 
    
    def confirmar_envio(driver, dados):
        try:

            driver.find_element_by_xpath(sendRequestReleaseTrip)
            if sendRequestReleaseTrip:
                driver.find_element_by_xpath(sendRequestReleaseTrip).click()
        
        except:
            textRelatorio = "Não foi possível confirmar a requisção de liberação da viagem"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Não foi possível confirmar a requisção de liberação da viagem', 'falhou': False},sys.exit() 
    
    
    def confirmar_espera(driver, dados):
        try:
            
            driver.find_element_by_xpath(confirm24hWait)
            if confirm24hWait:
                driver.find_element_by_xpath(confirm24hWait).click()

        except:
            textRelatorio = "Não foi possível confirmar a espera de 24 para liberação"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Não foi possível confirmar a espera de 24 para liberação', 'falhou': False},sys.exit() 
    
        else:
            textRelatorio = "Espera de 24 para liberação da corrida foi confirmada"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Liberacao de corrida - Motorista",nomeApp=['nomeApp'], status= "Sucesso")
            return {'mensagem': 'Espera de 24 para liberação da corrida foi confirmada', 'falhou': False},sys.exit() 