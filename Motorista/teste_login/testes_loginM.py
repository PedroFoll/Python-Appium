#Não existe error
from appium.webdriver import Remote
import sys
from time import sleep

from sqlalchemy import true
from geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from Motorista.teste_login.variaveisCadastro import*
from Motorista.teste_login.variaveisProfileMenu import*
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
            textRelatorio = "<li> ERRO Ao encontrar o botão de login - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Ao encontrar o botão de login', 'falhou': False}


    def clickando_botao_login(driver,dados):
        try:
            
            driver.implicitly_wait(20)
            driver.find_element_by_xpath(botaoLoginM).click()
            return True
        except Exception:

            textRelatorio = "<li> ERRO Ao clickar em login - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'botão de login não encontrado', 'falhou': False}


    def inserindo_credenciais(driver, dados):
        try:
            
            sleep(10)
            driver.find_element_by_xpath(campoEmailM).send_keys("peddro.foll@gmail.com")
            print("Inserindo Email")            
            driver.find_element_by_xpath(campoSenhaM).send_keys("123456")
            print("Inserindo Senha")           
            return True
        except Exception:
            
            textRelatorio = "<li> Não foi possivel inserir as credenciais - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Não foi possivel inserir as credenciais', 'falhou': False}, quit()

    def clicando_logar(driver,dados):
        try:
            driver.find_element_by_xpath (botaoLogarM)
            if botaoLogarM:
                driver.find_element_by_xpath (botaoLogarM).click()
                sleep(5)
                try:
                    driver.find_element_by_xpath(attentionmodal)
                except:
                    print("Login funcionou")
                    textRelatorio = "<li> Login realizado - Sucesso</li>"
                    GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    return {'Mensagem': 'Login realizado', 'Sucesso': True}
                else:
                    print("Login deu errado")
                    textRelatorio = "<li> Login invalido ou falta de conexão com a internet - FALHOU</li>"
                    return {'Mensagem': 'Login invalido ou falta de conexão com a internet', 'falhou': False}, quit()
                            
        except:
            print("Finalizando função")
            sleep(10)
            textRelatorio += "<li> Não foi possivel logar - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Não foi possivel logar', 'falhou': False}, quit()  

    def aceitando_permissao(driver,dados):
        try:

            driver.find_element_by_xpath(permissaoLocal).click()
            print("Aceitando permissão")
        except Exception:

            textRelatorio += "<li> Não foi possível aceitar a permissão de localização1 - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)

    def Permissao_Local(driver,dados):
        try:

            driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']").click()
            print("Aceitando permissão 2")
        except Exception:

            textRelatorio += "<li> Não foi possível aceitar a permissão de localização2- FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)

    
    def Permissao_Sobreposicao(driver,dados):
        try:

            driver.find_element_by_xpath(botao_segundo_plano).click()
            print("Permissão Sobreposição")
        except Exception:

            textRelatorio += "<li> Permissão de sobreposição já foi concedida </li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)

    def Permissao_All_Time(driver, dados):
        try:
            
            driver.find_element_by_xpath(permissaoTodoTempo)
            if permissaoTodoTempo:
                driver.find_element_by_xpath(permissaoTodoTempo).click()
                print("Permissao de Uso a todo momento")
                try:
                    driver.find_element_by_xpath(allowUseMidia)
                    if allowUseMidia:
                        driver.find_element_by_xpath(allowUseMidia).click()
                except:
                    print(" erro ao tentar permitir o uso de midia")
                    textRelatorio += '<li>Permissao ao uso de midia ja concedido</li>'
                    GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
                    
            
            textRelatorio = '<li>Login realizado com Sucesso</li>'
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'mengagem': 'Todas as permissões foram concedidas', 'sucesso': True, 'driver': driver}
        
        except:

            textRelatorio = "<li> Não foi possivel logar no motorista - FALHOU</li>"
            GerandoRelatorio.gerando_pasta_relatorio(driver, dados, textRelatorio)
            return {'Mensagem': 'Não foi possível Logar no motorista','falhou': False}

#Funcionando