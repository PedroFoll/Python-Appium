from teste_login.variaveisAceitandoCorridas import*
from teste_login.variaveisProfileMenu import*
from teste_login.variaveisCadastro import*
from appium.webdriver import Remote
from helpers.helpers import Helpers
from selenium.webdriver.support.ui import WebDriverWait
from teste_login.testes_login import Teste_Login
######################################WDW

espera = WebDriverWait(Teste_Login.Driver, 15)
######################################WDW

class Clickando_Login():
    def clickando_Para_Logar(webdriver):
        clickLoginButton = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]")
        return bool (clickLoginButton)
    espera.until(clickando_Para_Logar)