from selenium.webdriver.support.ui import WebDriverWait
from functions import*
from variaveisCadastro import*

wdw = WebDriverWait(driver, 10)

def click_register_button(webdriver):
    clickButton = driver.find_element_by_xpath(register)
    return bool (clickButton)

wdw.until(click_register_button)
try:
    clickButton = driver.find_element_by_xpath(register).click()
except:
    print("Não foi possível entrar no cadastro")
else:
    print("Foi possivel entrar no cadastro")