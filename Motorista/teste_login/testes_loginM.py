#Não existe error
from cgitb import text
import sys
from time import sleep
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.variaveis.variaveis import*
from helpers.helpers import Helpers
from maindriver import Driver



class Teste_Login():


    def Logando_Motorista(dados):
        
        driver = Driver.driver(dados)
        driver.implicitly_wait(20)
        sleep(5)

        localizando = Teste_Login.localizando_elemento(driver, dados)
        if localizando:
            Teste_Login.clickando_botao_login(driver, dados)
            Teste_Login.inserindo_credenciais(driver, dados)
            Teste_Login.clicando_logar(driver, dados)
            Teste_Login.aceitando_permissao(driver, dados)
            Teste_Login.Permissao_Local(driver, dados)
            Teste_Login.Permissao_Sobreposicao(driver, dados)

            return Teste_Login.Permissao_All_Time(driver, dados)


    def localizando_elemento(driver,dados):
        try:
            
            driver.find_element_by_xpath(botaoLoginM)
            return bool
        except Exception:
            textRelatorio = 'ERRO Ao encontrar botão de login'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 



    def clickando_botao_login(driver,dados):
        try:
            
            driver.implicitly_wait(20)
            driver.find_element_by_xpath(botaoLoginM).click()
            return True
        except Exception:
            textRelatorio = 'Nao foi possivel clickar em logar'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'botão aceite não encontrado', 'falhou': False},sys.exit() 


    def inserindo_credenciais(driver, dados):
        try:
            
            sleep(10)
            driver.find_element_by_xpath(campoEmailM).send_keys("peddro.foll@gmail.com")
            print("Inserindo Email")            
            driver.find_element_by_xpath(campoSenhaM).send_keys("123456")
            print("Inserindo Senha")           
            return True
        except Exception:
            textRelatorio = 'Nao foi possivel clickar em logar'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel inserir os dados de login do motorista', 'falhou': False},sys.exit() 

    def clicando_logar(driver,dados):
        try:
            sleep(15)
            driver.find_element_by_xpath (botaoLogarM)
            if botaoLogarM:
                driver.find_element_by_xpath (botaoLogarM).click()
                try:
                    driver.find_element_by_xpath(attentionmodal)
                    if attentionmodal:
                        textRelatorio = 'Sem conexão com internet, ou senha invalada'
                        GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
                        return {'mensagem': 'Nao foi possivel inserir os dados de login do motorista', 'falhou': False},sys.exit() 

                except Exception as sucesso:
                    return sucesso
        except:
            textRelatorio = 'Nao foi possivel logar'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel inserir os dados de login do motorista', 'falhou': False},sys.exit() 


    def aceitando_permissao(driver,dados):
        try:

            driver.find_element_by_xpath(permissaoLocal).click()
            print("Aceitando permissão")
        except Exception:

            textRelatorio = 'Campo informando que será utilizado a localização não encontrado'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel inserir os dados de login do motorista', 'falhou': False},sys.exit() 

    def Permissao_Local(driver,dados):
        try:

            driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']").click()
            print("Aceitando permissão 2")
        except Exception:

            textRelatorio = 'Campo de permissão de localização não encontrado'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel inserir os dados de login do motorista', 'falhou': False},sys.exit() 



    def Permissao_Sobreposicao(driver,dados):
        try:

            driver.find_element_by_xpath(botao_segundo_plano).click()
            print("Permissão Sobreposição")
        except Exception:

            return "Permissão de sobreporsião de aplicativos não foi solicitada"
            
    def Permissao_All_Time(driver, dados):
        try:
            
            driver.find_element_by_xpath(permissaoTodoTempo)
        except:
            textRelatorio = 'Nao foi possivel realizar o login'
            GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Falhou")
            return {'mensagem': 'Nao foi possivel inserir os dados de login do motorista', 'falhou': False},sys.exit() 

        
        else:
            if permissaoTodoTempo:
                driver.find_element_by_xpath(permissaoTodoTempo).click()
                try:
                    driver.find_element_by_xpath(allowUseMidia)
                    if allowUseMidia:
                        driver.find_element_by_xpath(allowUseMidia).click()
                except:
                    print("foi")
                    textRelatorio = 'Login realizado com sucesso'
                    GerandoRelatorio.enviando_dados_db(driver, dados = dados, textRelatorio= textRelatorio, nome_relatorio="Teste de Login - Motorista",nomeApp=['nomeApp'], status= "Sucesso")
                    return {'driver': driver}
#Funcionando