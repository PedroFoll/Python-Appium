from appium.webdriver.common.touch_action import TouchAction
from Motorista.teste_login.testes_loginM import Teste_Login
from Motorista.teste_login.acoes_na_tela import Mover_tela
from time import sleep


class Finalizar_chamado:

    def finalizando_chamado(dados):

        executandologin = Teste_Login.Logando_Motorista(dados)
        driver = executandologin['driver']
        driver.implicitly_wait(20)

        localizando = Finalizar_chamado.localizando_elemento(driver, dados)
        if localizando:
            Finalizar_chamado.iniciar_corrida(driver, dados)
            Finalizar_chamado.finalizando_corrida(driver, dados)

            return Finalizar_chamado.fechando_resumo_viagem(driver,dados)

    def iniciar_corrida(driver, dados):
        Mover_tela.iniciar_corrida(driver)
