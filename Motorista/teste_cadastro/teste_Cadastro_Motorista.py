
from appium.webdriver import Remote
import sys
from time import sleep
from Motorista.variaveis.variaveis import*
from appium.webdriver.common.touch_action import TouchAction
from helpers.geradorcpf import cpf_validado
from helpers.helpers import Helpers

class Teste_Cadastro_Motorista():


    def Driver(args):

        driver=Remote(
                    'http://localhost:4723/wd/hub',
                    {
                    "platformName": "android",
                    "appium:deviceName": "AppiumP",
                    "appium:app": args['url'],
                    "appium:avd": "Nexus_5_API_29",
                    #"isHeadless": True,
                    #"avdArgs":"-no-window"
                    })

        return driver

    def Cadastrando_Motorista(dados):

        driver = Teste_Cadastro_Motorista.Driver(dados)
        sleep(5)

        localizando = Teste_Cadastro_Motorista.localizando_elemento(driver, dados)
        if localizando:

            Teste_Cadastro_Motorista.Clicando_Para_Registrar(driver, dados)
            Teste_Cadastro_Motorista.Carregando_Tipos(driver, dados)
            Teste_Cadastro_Motorista.Dados_Pessoais(driver, dados)
            Teste_Cadastro_Motorista.Inserindo_Senha(driver, dados)
            Teste_Cadastro_Motorista.Selecionando_Cidade(driver, dados)
            Teste_Cadastro_Motorista.Aceitando_Termos(driver, dados)
            Teste_Cadastro_Motorista.Enviar_Foto(driver, dados)
            Teste_Cadastro_Motorista.Enviando_Dados_Carro(driver, dados)
            Teste_Cadastro_Motorista.Enviar_Documentos_CNH(driver, dados)
            Teste_Cadastro_Motorista.Enviar_Documentos_CRLV(driver, dados)
            Teste_Cadastro_Motorista.Enviar_Documentos_Antescedentes(driver, dados)
            Teste_Cadastro_Motorista.Enviar_Documentos_Comp_Adress(driver, dados)
            Teste_Cadastro_Motorista.Concluindo_Cadastro(driver,dados)



            return "Teste cadastro motorista"
        else:
            
            
            
            sys.exit()
    def localizando_elemento(driver,dados):
        try:
            
            sleep(5)
            driver.find_element_by_xpath(register)
            return{'mensagem':'Botão de registrar localizado', 'sucesso':'True'}
        except Exception as erro:
            return erro
            

    def Clicando_Para_Registrar(driver,dados):
        try:

            driver.implicitly_wait(20)
            driver.find_element_by_xpath(register).click()
            sleep(10)
        except Exception as erro:

            textRelatorio = "<li> ERRO Ao clickar em registrar - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'botão de registrar não encontrado', 'falhou': False}, erro
        else:
            return True     

    def Carregando_Tipos(driver,dados):
        try:
            print("entrando tipo")
            driver.implicitly_wait(20)
            driver.find_element_by_xpath(driverType).click()
            print("tipo motorista")
        except Exception as erro:
            textRelatorio = "<li> ERRO AO DEFINIR TIPO DE MOTORISTA - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Não foi possivel defirnir tipo de motorista', 'falhou': False}, erro, sys.exit()
        else:
            return True     

    def Dados_Pessoais(driver, dados):
        try:

            driver.find_element_by_xpath(toTypeName).send_keys("Homologação Fb704")
            sleep(3)            
        except Exception as erro:
            textRelatorio = "<li> ERRO TELA DE ENVIO DE DADOS NÃO FOI ENCONTRADO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Tela de envio de dados não foi carregada', 'falhou': False}, erro, sys.exit()

        try:

            driver.find_element_by_xpath(toTypeCpf).send_keys(cpf_validado)
            sleep(3)
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR O CPF - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR O CPF', 'falhou': False}, erro, sys.exit()
        
        try:

            driver.find_element_by_xpath(toTypeEmail).send_keys(Helpers.gerador_email())
            sleep(3)
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR O EMAIL - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR O EMAIL', 'falhou': False}, erro, sys.exit()
        
        try:
            
            driver.find_element_by_xpath(toTypePhone).send_keys("85997830980")
            sleep(3)
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR O TELEFONE - FALHOU</li>"
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR O TELEFONE', 'falhou': False}, erro, sys.exit()

        try:
            
            driver.find_element_by_xpath(toSetGender1).click()
            sleep(2)
            driver.find_element_by_xpath(toSetGender2).click()
            sleep(5)
        except Exception as erro:
            textRelatorio = "<li> NÃO FOI POSSIVEL DEFINIR O GENERO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL DEFINIR O GENERO', 'falhou': False}, erro, sys.exit()
        
        try:
            driver.find_element_by_xpath(toTypeEmail).click()
            sleep(5)
            nextButton01=driver.find_element_by_xpath(nextButton00)
            nextButton01.click()
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL AVANAÇAR PARA TELA SEGUINTE - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL AVANAÇAR PARA TELA SEGUINTE', 'falhou': False}, erro, sys.exit()
        
        else:
            sleep(3)
            nextButton01.click()
            return True


    def Inserindo_Senha(driver, dados):
        try:

            driver.implicitly_wait(10)
            driver.find_element_by_xpath(toTypePassword).send_keys("123456")
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR A SENHA - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR A SENHA', 'falhou': False}, erro, sys.exit()
    
        try:

            sleep(2)
            driver.find_element_by_xpath(toConfirmPassword).send_keys("123456")
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL CONFIRMAR O PASSWORD  - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL CONFIRMAR O PASSWORD', 'falhou': False}, erro, sys.exit()
        else:
            nextButton= driver.find_element_by_xpath(toContinue)
            nextButton.click()
            return True

    
    def Selecionando_Cidade(driver, dados):
        try:
            
            driver.find_element_by_xpath(citySelector1).click()
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O CAMPO DA CIDADE- FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O CAMPO DA CIDADE', 'falhou': False}, erro, sys.exit()
        
        try:
            
            sleep(3)
            driver.find_element_by_xpath(citySelector2).click()
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL SELECIONAR A CIDADE - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL SELECIONAR A CIDADE', 'falhou': False}, erro, sys.exit()
        else:
            nextButton= driver.find_element_by_xpath(toContinue)
            nextButton.click()
            sleep(10)

    
    def Aceitando_Termos(driver, dados):

        try:

            driver.find_element_by_xpath(termsTitle)
            if termsTitle:
                actions = TouchAction(driver)
                actions.press(x=714, y=1594)
                actions.move_to(x=717, y=662)
                actions.release() 
                actions.perform()
                sleep(1)
            else:
                textRelatorio = "<li>  ERRO NÃO FOI POSSIVEL DESCER A TELA DE TERMOS- FALHOU</li>"
                #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                return {'Mensagem': 'NÃO FOI POSSIVEL DESCER A TELA DE TERMOS', 'falhou': False}, erro, sys.exit()
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL SELECIONAR IDENTIFICAR A TELA DE TERMOS - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL SELECIONAR IDENTIFICAR A TELA DE TERMOS', 'falhou': False}, erro, sys.exit()
        
        try:
        
            driver.find_element_by_xpath(useTerms).click()
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O CAMPO PARA ACEITAR TERMOS - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O CAMPO PARA ACEITAR TERMOS', 'falhou': False}, erro, sys.exit()
        
        else:
            nextButton= driver.find_element_by_xpath(toContinue)
            nextButton.click()
            sleep(4)


    def Enviar_Foto (driver, dados):
        try:

            driver.find_element_by_xpath(toAcessCamera)
            sleep(3)
            if toAcessCamera:
                try:

                    driver.find_element_by_xpath(toAcessCamera).click()
                    sleep(3)
                except Exception as erro:
                    textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ABRIR A CAMERA - FALHOU</li>"
                    #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'NÃO FOI POSSIVEL ABRIR A CAMERA', 'falhou': False}, erro, sys.exit()


            try:
                #SE TRATA DE UMA PERMISSÃO DO USO DA CAMERA AO ANDROID
                #LOGO NÃO PRECISA DE SYS.EXIT, CASO NÃO SEJA IDENTIFICADO
                driver.find_element_by_xpath(allowCamera)
                sleep(3)
                if allowCamera:
                    try:

                        driver.find_element_by_xpath(allowCamera).click()
                        sleep(3)
                    except Exception as erro:
                        textRelatorio = "<li> ERRO NÃO FOI POSSIVEL DAR ACESSO A CAMERA - FALHOU</li>"
                        #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                        return {'Mensagem': 'NÃO FOI POSSIVEL DAR ACESSO A CAMERA', 'falhou': False}, erro, sys.exit()

            except Exception as erro:
                    textRelatorio = "<li> NÃO FOI POSSIVEL IDENTIFICAR CAMPO DE ACESSO A CAMERA</li>"
                    #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'NÃO FOI POSSIVEL IDENTIFICAR CAMPO DE ACESSO A CAMERA', 'falhou': False}

            
            try:

                driver.find_element_by_xpath(cammeraButton)
                sleep(3)
                if cammeraButton:
                    driver.find_element_by_xpath(cammeraButton).click()
                    sleep(3)
                else:
                    textRelatorio = "<li> ERRO NÃO FOI POSSIVEL  BATER A FOTO - FALHOU</li>"
                    #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'NÃO FOI POSSIVEL  BATER A FOTO', 'falhou': False}, erro, sys.exit()

            except Exception as erro:
                    textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA BATER A FOTO - FALHOU</li>"
                    #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA BATER A FOTO', 'falhou': False}, erro, sys.exit()

            else:
                sleep(5)

            try:

                driver.find_element_by_xpath(photoConfirm)
                if photoConfirm:
                    driver.find_element_by_xpath(photoConfirm).click()
                    sleep(3)
                else:
                    textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENVIAR A FOTO - FALHOU</li>"
                    #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'NÃO FOI POSSIVEL ENVIAR A FOTO', 'falhou': False}, erro, sys.exit()

            except Exception as erro:
                    textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA ENVIO - FALHOU</li>"
                    #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O BOTAO PARA ENVIO', 'falhou': False}, erro, sys.exit()

        except Exception as erro:

            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ACESSAR A CAMERA - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ACESSAR A CAMERA', 'falhou': False}, erro, sys.exit()

        else:

            nextButton= driver.find_element_by_xpath(toContinue)
            nextButton.click()
            sleep(5)

    def Enviando_Dados_Carro(driver, dados):
        try:
            
            driver.find_element_by_xpath(vehicleBrand).send_keys("Fiat")
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR A MARCA- FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR A MARCA', 'falhou': False}, erro, sys.exit()

        try:
            
            driver.find_element_by_xpath(vehicleModel).send_keys("Uno da 704Apps")
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR O MODELO DO CARRO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR O MODELO DO CARRO', 'falhou': False}, erro, sys.exit()

        try:
            
            driver.find_element_by_xpath(vehiclePlate).send_keys("TST-0704")
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR A PLACA - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR A PLACA', 'falhou': False}, erro, sys.exit()

        try:
        
            driver.find_element_by_xpath(vehicleVinNumber).send_keys("12171174856")
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR O RENAVAM - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR O RENAVAM', 'falhou': False}, erro, sys.exit()


        try:

            driver.find_element_by_xpath(vehicleColor).send_keys('Azul')
        except Exception as erro:
            textRelatorio = "<li> NÃO FOI POSSIVEL INSERIR A COR DO CARRO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR A COR DO CARRO', 'falhou': False}, erro, sys.exit()

        try:

            driver.find_element_by_xpath(vehicleSeatsNumber).send_keys('5')
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL DEFINIR A QUANTIDADE DE ACENTOS DO VEICULO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL DEFINIR A QUANTIDADE DE ACENTOS DO VEICULO', 'falhou': False}, erro, sys.exit()

        try:
            
            driver.find_element_by_xpath(vehicleYear).send_keys('2018')
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL DEFINIR O ANO DO CARRO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL DEFINIR O ANO DO CARRO', 'falhou': False}, erro, sys.exit()
        else:
            nextButton= driver.find_element_by_xpath(toContinue)
            nextButton.click()
            sleep(5)
        
    def Enviar_Documentos_CNH(driver, dados):

        try:

            driver.find_element_by_xpath(toTypeCnhField)
            sleep(3)
            if toTypeCnhField:
                driver.find_element_by_xpath(toTypeCnhField).send_keys("69432109613")
                sleep(3)
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O CAMPO PARA INSERIR A CNH - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O CAMPO PARA INSERIR A CNH ', 'falhou': False}, erro, sys.exit()
        
        try:

            driver.find_element_by_xpath(documentsSendFotos)
            sleep(3)
            if documentsSendFotos:
                driver.find_element_by_xpath(documentsSendFotos).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O CAMPO PARA ENVIAR A FOTO DA CNH - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O CAMPO PARA ENVIAR A FOTO DA CNH ', 'falhou': False}, erro, sys.exit()


        try:

            driver.find_element_by_xpath(cammeraButton)
            sleep(3)
            if cammeraButton:
                driver.find_element_by_xpath(cammeraButton).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL  BATER A FOTO DA CNH - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL  BATER A FOTO DA CNH', 'falhou': False}, erro, sys.exit()

        
        try:
            
            driver.find_element_by_xpath(photoConfirm)
            sleep(3)
            if photoConfirm:
                driver.find_element_by_xpath(photoConfirm).click()
                sleep(3)
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENVIAR A FOTO DA CNH - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENVIAR A FOTO DA CNH', 'falhou': False}, erro, sys.exit()
        
        else:
            driver.find_element_by_xpath(toContinueButtonDocuments).click()
            sleep(3)

    def Enviar_Documentos_CRLV(driver, dados):

        try:

            driver.find_element_by_xpath(toTypeCrlvField)
            sleep(3)
            if toTypeCrlvField:
                driver.find_element_by_xpath(toTypeCrlvField).send_keys('Teste fabrica 704')
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR O CRLV - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR O CRLV', 'falhou': False}, erro, sys.exit()
        
        try:

            driver.find_element_by_xpath(documentsSendFotos)
            sleep(3)
            if documentsSendFotos:
                driver.find_element_by_xpath(documentsSendFotos).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL IDENTIFICAR O CAMPO PARA ENVIO DE IMAGENS DA CLRV - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL IDENTIFICAR O CAMPO PARA ENVIO DE IMAGENS DA CLRV', 'falhou': False}, erro, sys.exit()
        
        try:

            driver.find_element_by_xpath(cammeraButton)
            sleep(3)
            if cammeraButton:
                driver.find_element_by_xpath(cammeraButton).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL  BATER A FOTO DO CRLV - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL  BATER A FOTO DO CRLV', 'falhou': False}, erro, sys.exit()

        
        try:
            
            driver.find_element_by_xpath(photoConfirm)
            sleep(3)
            if photoConfirm:
                driver.find_element_by_xpath(photoConfirm).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENVIAR A FOTO DO CRLV - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENVIAR A FOTO DO CRLV', 'falhou': False}, erro, sys.exit()

        else:
            driver.find_element_by_xpath(toContinueButtonDocuments).click()
            sleep(3)

    def Enviar_Documentos_Antescedentes(driver, dados):
        try:
            
            driver.find_element_by_xpath(toTypeCriminalPastField)
            sleep(3)
            if toTypeCriminalPastField:
                driver.find_element_by_xpath(toTypeCriminalPastField).send_keys('Teste fabrica 704')
                sleep(3)

        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL INSERIR OS ANTECEDENTES CRIMINAIS - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL INSERIR OS ANTECEDENTES CRIMINAIS', 'falhou': False}, erro, sys.exit()
        
        try:

            driver.find_element_by_xpath(documentsSendFotos)
            sleep(3)
            if documentsSendFotos:
                driver.find_element_by_xpath(documentsSendFotos).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ACESSAR O CAMPO PARA ENVIAR A FOTO DOS ANTECEDENTES CRIMINAIS - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ACESSAR O CAMPO PARA ENVIAR A FOTO DOS ANTECEDENTES CRIMINAIS', 'falhou': False}, erro, sys.exit()
        
        try:

            driver.find_element_by_xpath(cammeraButton)
            sleep(3)
            if cammeraButton:
                driver.find_element_by_xpath(cammeraButton).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL  BATER A FOTO DOS ANTECEDENTES CRIMINAIS - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL  BATER A FOTO DOS ANTECEDENTES CRIMINAIS', 'falhou': False}, erro, sys.exit()

        
        try:
            
            driver.find_element_by_xpath(photoConfirm)
            sleep(3)
            if photoConfirm:
                driver.find_element_by_xpath(photoConfirm).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENVIAR A FOTO DOS ANTECEDENTES CRIMINAIS - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENVIAR A FOTO DOS ANTECEDENTES CRIMINAIS', 'falhou': False}, erro, sys.exit()
        
        else:
            driver.find_element_by_xpath(toContinueButtonDocuments).click()
            sleep(5)


    def Enviar_Documentos_Comp_Adress(driver, dados):
        try:
            
            driver.find_element_by_xpath(proofOfAddress)
            sleep(3)
            if proofOfAddress:
                driver.find_element_by_xpath(proofOfAddress).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ACESSAR O CAMPO PARA ENVIAR A FOTO DO COMPROVANTE DE ENDEREÇO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ACESSAR O CAMPO PARA ENVIAR A FOTO DO COMPROVANTE DE ENDEREÇO', 'falhou': False}, erro, sys.exit()
        
        try:

            driver.find_element_by_xpath(cammeraButton)
            sleep(3)
            if cammeraButton:
                driver.find_element_by_xpath(cammeraButton).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL  BATER A FOTO DO COMPROVANTE DE ENDEREÇO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL  BATER A FOTO COMPROVANTE DE ENDEREÇO', 'falhou': False}, erro, sys.exit()
     
        try:
            
            driver.find_element_by_xpath(photoConfirm)
            sleep(3)
            if photoConfirm:
                driver.find_element_by_xpath(photoConfirm).click()
                sleep(3)
        
        except Exception as erro:
            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENVIAR A FOTO COMPROVANTE DE ENDEREÇO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENVIAR A FOTO COMPROVANTE DE ENDEREÇO', 'falhou': False}, erro, sys.exit()

        else:
            driver.find_element_by_xpath(toContinueButtonDocuments).click()
            sleep(10)


    def Concluindo_Cadastro(driver, dados):
        try:

            driver.find_element_by_xpath(lastNextButton)
            if lastNextButton:
                driver.find_element_by_xpath(lastNextButton).cick()

        except Exception as erro:

            textRelatorio = "<li> ERRO NÃO FOI POSSIVEL ENCONTRAR O BOTÃO PARA CONCLUIR CADASTRO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'NÃO FOI POSSIVEL ENCONTRAR O BOTÃO PARA CONCLUIR CADASTRO', 'falhou': False}, erro
        
        else:
            textRelatorio = "<li> TESTE CONCLUIDO COM SUCESSO - FALHOU</li>"
            #GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'TESTE CONCLUIDO COM SUCESSO', 'sucesso': True}

#######################################################################################################################################