from time import sleep
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.variaveis.variaveis import*
from Motorista.teste_login.testes_loginM import Teste_Login
from Motorista.enviando_mensagens.enviar_mensagens import Enviar_mensagem
from Motorista.teste_login.acoes_na_tela import Mover_tela
from os import sys

class Aceitar_corrida:
    
    
    def aceitando_corridas(dados):
        
        
        executandologin = Teste_Login.Logando_Motorista(dados)
        driver = executandologin['driver']
        driver.implicitly_wait(20)

        localizando = Aceitar_corrida.localizando_elemento(driver, dados)
        if localizando:
            Aceitar_corrida.sobrepondo_apps(driver, dados)
            Aceitar_corrida.aceitar_corrida(driver, dados)
            Enviar_mensagem.enviando_mensagem(driver, dados)
            
            return Aceitar_corrida.sinalizar_chegada(driver, dados)


    def localizando_elemento (driver, dados):

        try:

            driver.find_element_by_xpath(botaoStart)
        
        except Exception as erro:
            print(erro)
            textRelatorio = 'Botão de Iniciar nao encontrado'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de aceitar agendamento - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 

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

    
    def aceitar_corrida(driver, dados):
        x = 0
        while (x)<5:
            try:
                driver.find_element_by_xpath(callTrip)
                if callTrip:
                    driver.find_element_by_xpath(callTrip).click()
                    break
            except Exception as erro:
                print(erro)
                textRelatorio = 'Não foi possivel aceitar corrida'
                GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de aceitar agendamento - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                sleep(15)                
                x = x + 1 
        return {'mensagem': 'botão aceite não encontrado', 'Sucesso': True}

    def sinalizar_chegada(driver,dados):
        try:
            driver.find_element_by_xpath(slideButton)
            if slideButton:
                print('tentando mover')
                Mover_tela.iniciar_corrida(driver)
            return 'Deu certo, boy, vc conseguiu'

        except Exception as erro:
            print(erro)
        
        return 'Deu certo, boy, vc conseguiu'
