
from appium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait


driver = Remote(
    'http://127.0.0.1:4723/wd/hub',
    {
    'platformName': 'Android',
    'appium:deviceName': 'AppiumP',
    'appium:app': '/home/ulisses/Projetos/Estudos/testemobile/app-test.apk',
    'appium:avd': 'Pixel_5_API_29'
    }
    )


#início do relatório
textRelatorio = 'Início de relatório'

#configurações de cores no terminal

class TerminalColor:
    ERRO = '\033[91m' #cor vermelha
    NORMAL = '\033[0m' #cor branca 
    SUCESS = '\033[32m' #cor verde

#configuração do WebDriverWait

espera = WebDriverWait(driver, 10)

#estrutura dos testes

def selecionar_opcao_login(webdriver):
    botaoOpcaoLogin = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]")
    return bool (botaoOpcaoLogin)

espera.until(selecionar_opcao_login)
try:
    botaoOpcaoLogin = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]").click()
except:
    print(TerminalColor.ERRO+'ERRO - Não foi possível clicar no botão LOGIN - FALHOU'+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Não foi possível clicar no botâo LOGIN - FALHOU"
else:
    print(TerminalColor.SUCESS+'SUCESSO - Seleção de opção LOGIN realizada com SUCESSO'+TerminalColor.NORMAL)
    textRelatorio += "\nSUCESSO - Seleção de opção LOGIN realizada com SUCESSO"


def preencher_campo_login(webdriver):
    campoEmail = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[1]")
    return bool (campoEmail)

espera.until(preencher_campo_login)
try:
    campoEmail = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[1]").send_keys("motorista@teste.com")
except:
    print(TerminalColor.ERRO+"ERRO - Campo Email não encontrado - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "ERRO - Campo Email não encontrado - FALHOU"
else: 
    print(TerminalColor.SUCESS+"Campo email encontrado e preenchido com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "Campo email encontrado e preenchido com SUCESSO"

def selecionar_campo_senha(webdriver):
    campoSenha = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[2]")
    return bool (campoSenha)

espera.until(selecionar_campo_senha)
try:
    campoSenha = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[2]").send_keys("654321")
except:
    print(TerminalColor.ERRO+"ERRO - Não foi possível localizar campo SENHA - FALHOU"+TerminalColor.NOMRMAL)
    textRelatorio += "\nERRO - Não foi possível localizar campo SENHA - FALHOU"
else:
    print(TerminalColor.SUCESS+"Campo SENHA localizado e preenchido com sucesso"+TerminalColor.NORMAL)
    textRelatorio += "\nCampo SENHA localizado e preenchido com sucesso"



def clicando_botao_logar(webdriver):
    botaoLogar = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button")
    return bool (botaoLogar)

espera.until(clicando_botao_logar)
try: 
    botaoLogar = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.widget.Button").click()
except:
    print(TerminalColor.ERRO+"ERRO - Não foi possível clicar no botão LOGIN - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Não foi possível clicar no botão LOGIN - FALHOU"
else:
    print(TerminalColor.SUCESS+"Botão Login clicando com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nBotão Login clicando com SUCESSO"

textRelatorio += "\n TESTE DE LOGIN FINALIZADO COM SUCESSO"


with open("RelatorioModelo.txt", 'w') as arquivo:
    arquivo.write(textRelatorio)
