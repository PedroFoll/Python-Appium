import sys
from time import sleep
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.variaveis.variaveis import*
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
            
            return {Trocando_senha.preenchendo_Troca_Senha(driver, dados)}
    
    def localizando_elemento (driver, dados):

        try:

            driver.find_element_by_xpath(botaoStart)
            return True
        except Exception as erro:
            print(erro)
            textRelatorio = "Botão para ficar online não necontrando"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de troca de senha - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 

    def selecionando_Menu(driver, dados):
        try:

            TouchAction(driver).tap(x=970, y=206).perform()
        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao selecionar menu"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de troca de senha - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao selecionar menu', 'falhou': False},sys.exit() 
            
    def selecionando_Perfil(driver, dados):
        try:
            
            sleep(5)
            driver.find_element_by_xpath(profileButton).click()
        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao acessar Perfil"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de troca de senha - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao selecionar menu', 'falhou': False},sys.exit() 
            
    def clickando_Editar_Perfil(driver, dados):
        try:

            sleep(5)
            driver.find_element_by_xpath(editProfileButton).click()
            sleep(10)
        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao tentar editar o Perfil"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de troca de senha - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao tentar editar o Perfil', 'falhou': False},sys.exit() 
            
    def preenchendo_Troca_Senha(driver, dados):
        try:
            
            driver.find_element_by_xpath(currentPassword)
            if currentPassword:
                driver.find_element_by_xpath(currentPassword).send_keys('123456')
                

        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao identificar os campos de troca de senha"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de troca de senha - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao identificar os campos de troca de senha', 'falhou': False},sys.exit() 
            

        try:
            
            driver.find_element_by_xpath(newPassword)
            if newPassword:
                driver.find_element_by_xpath(newPassword).send_keys('123456')
                

        except Exception as erro:
            print(erro)
            textRelatorio = "Não foi possivel inserir a nova senha"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de troca de senha - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Não foi possivel inserir a nova senha', 'falhou': False},sys.exit() 
            
        try:
            driver.find_element_by_xpath(confirmationPassword)
            if confirmationPassword:
                driver.find_element_by_xpath(confirmationPassword).send_keys('123456')
                

        except Exception as erro:
            print(erro)
            textRelatorio = "Não foi possivel inserir a senha de confirmação"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de troca de senha - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Não foi possivel inserir a senha de confirmação', 'falhou': False},sys.exit() 
            
        else:
            driver.find_element_by_xpath(savePassword).click()
            textRelatorio = "Não foi possivel inserir a senha de confirmação"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de troca de senha - Motorista",nomeApp=['nomeApp'], status= "Sucesso")
            return {'mensagem': 'Não foi possivel inserir a senha de confirmação', 'Sucesso': True},sys.exit() 
            