from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.teste_login.testes_loginM import Teste_Login
from Motorista.teste_login.acoes_na_tela import Mover_tela
from helpers.helpers import Helpers
from helpers.geradorcpf import cpf_validado
from os import sys
from time import sleep
from Motorista.variaveis.variaveis import *


class Macaneta_manual:


    def Iniciando_macaneta(dados):


        executandologin = Teste_Login.Logando_Motorista(dados)
        driver = executandologin['driver']
        driver.implicitly_wait(20)

        localizando = Macaneta_manual.localizando_elemento(driver, dados)
        if localizando:
            Macaneta_manual.ficando_online(driver, dados)
            Macaneta_manual.sobrepondo_apps(driver,dados)
            Macaneta_manual.clickando_macaneta(driver, dados)
            Macaneta_manual.selecionando_tipo_corrida(driver, dados)
            Macaneta_manual.informando_endereço(driver, dados)
            Macaneta_manual.inserir_nome_cliente(driver, dados)
            Macaneta_manual.selecionar_pagamento(driver,dados)
            Macaneta_manual.confirmar_viagem(driver, dados)
            Macaneta_manual.começando_corrida(driver, dados)
            Macaneta_manual.finalizando_corrida(driver, dados)
        
        return "Deu bom boyzinho"

    
    def localizando_elemento(driver, dados):
        try:

            driver.find_element_by_xpath(botaoStart)
            return True
        except Exception as erro:
            print(erro)
            textRelatorio = "Botão para ficar online não necontrando"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 

    def ficando_online(driver,dados):
        try:

            driver.find_element_by_xpath(botaoStart)
            if botaoStart:
                driver.find_element_by_xpath(botaoStart).click()
        except Exception as erro:
            print(erro)
            textRelatorio = "Não consegui ficar online"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Não consegui ficar online', 'falhou': False},sys.exit()

    def sobrepondo_apps(driver, dados):
        try:

            driver.find_element_by_xpath(overOtherApps)
            if overOtherApps:
                driver.find_element_by_xpath(overOtherApps).click()
                sleep(5)
                driver.back()

        except:
            return "Permissão de sobreposição já consedida"


    def clickando_macaneta(driver, dados):
        sleep(10)
        Mover_tela.macaneta_manual(driver)

    def selecionando_tipo_corrida(driver, dados):
        try:

            driver.find_element_by_xpath(tipo_corrida)
            sleep(3)
            if tipo_corrida:
                driver.find_element_by_xpath(tipo_corrida).click()
                sleep(8)

        except :
            textRelatorio = "Nao foi possivel selecionar o tipo da corrida"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel selecionar o tipo da corrida', 'falhou': False},sys.exit()


    def informando_endereço(driver, dados):
        try:
            print("informando endereço")
            driver.find_element_by_xpath(destino)
            if destino:
                driver.find_element_by_xpath(destino).send_keys('North Shopping Fortaleza')
                sleep(5)
                driver.back()
                try:

                    driver.find_element_by_xpath(destino_resultado)
                    if destino_resultado:
                        driver.find_element_by_xpath(destino_resultado).click()
                except :
                    textRelatorio = "Nao foi possivel selecionar o endereço de destino"
                    GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                    return {'mensagem': 'Nao foi possivel selecionar o endereço de destino', 'falhou': False},sys.exit()


        
        except:
            textRelatorio = "Nao foi encontrado o campo para informar o endereço de destino"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi encontrado o campo para informar o endereço de destino', 'falhou': False},sys.exit()




    def inserir_nome_cliente(driver, dados):
        try:
            print('inserindo dados do cliente')
            sleep(8)
            driver.find_element_by_xpath(nome_cliente_macaneta)
            if nome_cliente_macaneta:
                driver.find_element_by_xpath(nome_cliente_macaneta).send_keys('Pedro Foll')
                sleep(1)
                driver.find_element_by_xpath(phone_cliente_macaneta).send_keys('85997830980')
                sleep(1)
                driver.find_element_by_xpath(cpf_cliente_macaneta).send_keys(cpf_validado)
                sleep(1)
                driver.find_element_by_xpath(email_cliente_macaneta).send_keys(Helpers.gerador_email())
                sleep(1)
                Mover_tela.movendo_dados_macaneta(driver)
                sleep(3)

        except :
            textRelatorio = "Nao foi possivel confirmar os dados do cliente"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel confirmar os dados do cliente', 'falhou': False},sys.exit()



    def selecionar_pagamento(driver, dados):

        try:
            sleep(8)
            driver.find_element_by_xpath(payment_form)
            if payment_form:
                driver.find_element_by_xpath(payment_form).click()
                try:
                    sleep(5)
                    driver.find_element_by_xpath(selecionando_dinheiro).click()
                except:
                    textRelatorio = "Nao foi possivel inserir forma de pagamento em dinheiro"
                    GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                    return {'mensagem': 'Nao foi possivel inserir forma de pagamento em dinheiro', 'falhou': False},sys.exit()
            else:
                driver.back()
                Mover_tela.movendo_dados_macaneta(driver)
                sleep(3)
                driver.find_element_by_xpath(payment_form).click()
                sleep(3)
                driver.find_element_by_xpath(selecionando_dinheiro).click()

        except:
            textRelatorio = "Nao foi possivel encontrar o campo para selecao de forma de pagamento"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel encontrar o campo para selecao de forma de pagamento', 'falhou': False},sys.exit()


    def confirmar_viagem(driver, dados):
        
        try:

            driver.find_element_by_xpath(confirmar_dados)
            if confirmar_dados:
                driver.find_element_by_xpath(confirmar_dados).click()
                sleep(20)

        except:
            textRelatorio = "Nao foi possivel confirmar os dados do cliente"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel confirmar os dados do cliente', 'falhou': False},sys.exit()

    def começando_corrida(driver,dados):
        try:

            driver.find_element_by_xpath(cliente_nome)
            if cliente_nome:
                print('tentando iniciar corrida')
                Mover_tela.usando_slide_button(driver)
                
        except:
            textRelatorio = "Nao foi possivel iniciar corrida"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel iniciar corrida', 'falhou': False}, sys.exit()

    def finalizando_corrida(driver, dados):        
        try:    
            driver.find_element_by_xpath(slideButton)
            if slideButton:
                Mover_tela.usando_slide_button(driver)
                try:
                    driver.find_element_by_xpath(closeResumTrip)
                    if closeResumTrip:
                        driver.find_element_by_xpath(closeResumTrip).click()

                except:
                    textRelatorio = "Nao foi possivel identificar o campo de resumo da viagem"
                    GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                    return {'mensagem': 'Nao foi possivel identificar o campo de resumo da viagem', 'falhou': False},sys.exit()

        except:
            textRelatorio = "Campo para finalizar a corrida não foi identificado"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Macaneta Manual - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Campo para finalizar a corrida não foi identificado', 'falhou': False},sys.exit()