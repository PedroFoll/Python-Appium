import sys
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from time import sleep
from Motorista.variaveis.variaveis import*
from Motorista.teste_login.testes_loginM import Teste_Login
from appium.webdriver.common.touch_action import TouchAction


class Mudar_Foto:

    
    def mudando_foto(dados):
        
        
        executandologin = Teste_Login.Logando_Motorista(dados)
        driver = executandologin['driver']
        driver.implicitly_wait(20)

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
            textRelatorio = "Botão para ficar online não necontrando"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 


    def selecionando_Menu(driver, dados):
        try:

            TouchAction(driver).tap(x=970, y=206).perform()
        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao selecionar menu"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao selecionar menu', 'falhou': False},sys.exit() 
                
    def selecionando_Perfil(driver, dados):
        try:
            
            sleep(5)
            driver.find_element_by_xpath(profileButton).click()
        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao acessar Perfil"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao selecionar menu', 'falhou': False},sys.exit() 
            

    def clickando_Editar_Perfil(driver, dados):
        try:

            sleep(5)
            driver.find_element_by_xpath(editProfileButton).click()
            sleep(10)
        except Exception as erro:
            print(erro)
            textRelatorio = "Erro ao tentar editar o Perfil"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Erro ao tentar editar o Perfil', 'falhou': False},sys.exit() 
            

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
                    textRelatorio = "Permissao ao uso de midia ja concedido"
                    return textRelatorio
            
            try:

                driver.find_element_by_xpath(cammeraButton)
                sleep(3)
                if cammeraButton:
                    driver.find_element_by_xpath(cammeraButton).click()
                    sleep(3)
                else:
                    textRelatorio = "NÃO FOI POSSIVEL  BATER A FOTO"
                    GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                    return {'mensagem': 'NÃO FOI POSSIVEL  BATER A FOTO', 'falhou': False},sys.exit() 
            

            except Exception as erro:
                print(erro)
                textRelatorio = "NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA BATER A FOTO"
                GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                return {'mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA BATER A FOTO', 'falhou': False},sys.exit() 
            
            else:
                sleep(5)
            try:

                driver.find_element_by_xpath(photoConfirm)
                sleep(3)
                if photoConfirm:
                        driver.find_element_by_xpath(photoConfirm).click()
                        sleep(3)
                else:
                    textRelatorio = "ERRO NÃO FOI POSSIVEL ENVIAR A FOTO"
                    GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                    return {'mensagem': 'ERRO NÃO FOI POSSIVEL ENVIAR A FOTO', 'falhou': False},sys.exit() 
            
            except Exception as erro:
                print(erro)
                textRelatorio = "NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA ENVIO"
                GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                return {'mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA ENVIO', 'falhou': False},sys.exit() 

            try:
                driver.find_element_by_xpath(confirmPictureSend)
                if confirmPictureSend:
                    driver.find_element_by_xpath(confirmPictureSend).click()
            except:
                print(erro)
                textRelatorio = "NÃO FOI POSSIVEL ENVIAR FOTO"
                GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                return {'mensagem': 'NÃO FOI POSSIVEL ENVIAR FOTO', 'falhou': False},sys.exit() 
                



        except:
            textRelatorio = "NÃO FOI ENCONTRADO CAMPO PARA MUDANÇA DE FOTO"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'NÃO FOI ENCONTRADO CAMPO PARA MUDANÇA DE FOTO', 'falhou': False},sys.exit() 
                
        else:
            textRelatorio = "SOLICITAÇÃO DE TROCA DE FOTO ENVIADA"
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Troca de foto - Motorista",nomeApp=['nomeApp'], status= "Sucesso")
            return {'mensagem': 'SOLICITAÇÃO DE TROCA DE FOTO ENVIADA', 'falhou': False},sys.exit() 
            