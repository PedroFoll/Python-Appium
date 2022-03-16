from appium.webdriver.common.touch_action import TouchAction
from Motorista.variaveis.variaveis import*
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



class Mover_tela():
    def movendo_para_baixo(driver):
        sleep(6)
        actions = TouchAction(driver)
        actions.press(x=494, y=1745)
        actions.move_to(x=508, y=296)
        actions.release() 
        actions.perform()
        sleep(2)
        actions = TouchAction(driver)
        actions.press(x=537, y=1756)
        actions.move_to(x=517, y=250)
        actions.release()
        actions.perform()
        sleep(5)

    def iniciar_corrida(driver):
        actions = ActionChains(driver)
        actions.click_and_hold(slideButton)
        actions.move_to(arrowIcon)
        actions.release() 
        actions.perform()

    def usando_slide_button(driver):
        actions= TouchAction(driver)
        actions.press(x=84, y=1661)
        actions.move_to(x=1013, y=1661)
        actions.release()
        actions.perform()

    
    def macaneta_manual(driver):
        action = TouchAction(driver)
        action.tap(x=946, y=1280).perform()
        sleep(5)
        action.tap(x=528, y=1353).perform()

    def movendo_dados_macaneta(driver):
        actions = TouchAction(driver)
        actions.press(x=24, y=1713)
        actions.move_to(x=33, y=615)
        actions.release() 
        actions.perform()