from argparse import Action
from time import sleep
from Motorista.variaveis.variaveis import*
#from appium.webdriver.common.touch_action import TouchAction
#TouchAction usado para entar fazer com que seja pressionado o botão para envio de audio

class Enviar_mensagem:


    def enviando_mensagem(driver, dados):
        
        driver.implicitly_wait(20)

        localizando = Enviar_mensagem.localizando_elemento(driver, dados)
        if localizando:
            Enviar_mensagem.abrindo_chat(driver, dados)
            Enviar_mensagem.permitir_midia(driver, dados)
            Enviar_mensagem.permitir_audio(driver, dados)
            Enviar_mensagem.escrevendo_mensagem(driver, dados)
            Enviar_mensagem.verificando_envio(driver, dados)
            
            return Enviar_mensagem.voltando_tela_corrida(driver, dados)

    def localizando_elemento(driver,dados):
        try:
            driver.find_element_by_xpath(chatBubble)
            return "Deu bom boy"
        except Exception as erro:
            print(erro)
            return "Deu ruim boy ao tentar encontrar o icone de chat", quit()


    def abrindo_chat(driver, dados):
        try:

            driver.find_element_by_xpath(chatBubble)
            if chatBubble:
                driver.find_element_by_xpath(chatBubble).click() 
                return "Deu bom boy"
        except Exception as erro:
            print(erro)
            return "Deu ruim boy erro ao tentar abrir o chat", quit()

    def permitir_midia(driver, dados):
        try:
            driver.find_element_by_xpath(allowUseMidia)
            if allowUseMidia:
                driver.find_element_by_xpath(allowUseMidia).click()
                return "Deu bom boy"
        except:
            return "Permissão de midia já consedida"

    def permitir_audio(driver, dados):
        try:
          
            driver.find_element_by_xpath(allowRecordAudio)
            if allowRecordAudio:
                driver.find_element_by_xpath(allowRecordAudio).click()
                return "Deu bom boy"
        except Exception as erro:
            print(erro)        
            return "Deu ruim boy ao tentar permitir o uso do microfone",quit()

    def escrevendo_mensagem(driver, dados):
        try:

            driver.find_element_by_xpath(fieldOfText)
            if fieldOfText:
                driver.find_element_by_xpath(fieldOfText).send_keys("Olá, isso é um teste da 704Apps")
                sleep(5)
                driver.find_element_by_xpath(toSendTheMsg).click()                
                return "Deu bom boy"
        except Exception as erro:
            print(erro)
            return "Deu ruim boy ao tentar escrever a mensagem",quit()

    """ def enviando_audio(driver,dados):
        try:
            driver.find_element_by_xpath(toSendRecordAudio)
            if toSendRecordAudio:
            
                action = TouchAction(driver)
                driver.find_element_by_xpath(toSendRecordAudio)
                action.long_press(toSendRecordAudio)
                action.realese()
                action.perform()

                return "Deu bom boy"
        except Exception as erro:
            print(erro)
            return "Deu ruim no envio do audio"
 """
    def verificando_envio(driver, dados):
        try:
            driver.find_element_by_xpath(theSentMsg)
            if theSentMsg:
                print(987)
                return "deu bom"
        except:
            print(123)
            return "deu ruim ao verificar se a mensagem foi enviada",quit()

    def voltando_tela_corrida(driver,dados):
        try:


            driver.find_element_by_xpath(toBackButton)
            if toBackButton:
                driver.find_element_by_xpath(toBackButton).click()
                return {'mensagem':'Deu tudo certo', 'driver':driver}
        except Exception as erro:
            return "Deu ruim boy"