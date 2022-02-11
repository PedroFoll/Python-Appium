
from appium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


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

#REALIZANDO LOGIN
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
    campoEmail = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[1]").send_keys("ulisses1991@gmail.com")
except:
    print(TerminalColor.ERRO+"ERRO - Campo Email não encontrado - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Campo Email não encontrado - FALHOU"
else: 
    print(TerminalColor.SUCESS+"Campo email encontrado e preenchido com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nCampo email encontrado e preenchido com SUCESSO"

def selecionar_campo_senha(webdriver):
    campoSenha = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[2]")
    return bool (campoSenha)

espera.until(selecionar_campo_senha)
try:
    campoSenha = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText[2]").send_keys("123456")
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


#aceitando permissões 
#ACEITANDO PERMISSÕES
sleep(4)

def aceitando_permissao_localizacao(webdriver):
    clickYesLocation = webdriver.find_element_by_xpath("//android.view.View[@resource-id='optionAcceptedLocalBackground']")
    return bool (clickYesLocation)

espera.until(aceitando_permissao_localizacao)
try:
    clickYesLocation=driver.find_element_by_xpath("//android.view.View[@resource-id='optionAcceptedLocalBackground']").click()
except:
    print(TerminalColor.ERRO+"ERRO - Não foi possível aceitar a permissão de localização - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Não foi possível aceitar a permissão de localização - FALHOU"
else: 
    print(TerminalColor.SUCESS+"Permissão uso da localização foi aceita com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nPermissão uso da localização foi aceita com SUCESSO"


sleep(1)


def Permissao_Local(webdriver):
  allowWhileUseApp = webdriver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
  return bool (allowWhileUseApp)

espera.until(Permissao_Local)
try:
    allowWhileUseApp = driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']").click()
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao conceder permissão - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao conceder permissão - FALHOU"
else: 
    print(TerminalColor.SUCESS+"Concessão de Permissão realizada com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nConcessão de Permissão realizada com SUCESSO"


def aceitando_permissao_localizacao(webdriver):
    clickYesLocation = webdriver.find_element_by_xpath("//android.view.View[@resource-id='optionAcceptedLocalBackground']")
    return bool (clickYesLocation)

espera.until(aceitando_permissao_localizacao)
try:
    clickYesLocation = driver.find_element_by_xpath("//android.view.View[@resource-id='optionAcceptedLocalBackground']").click()
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao conceder permissão - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao conceder permissão - FALHOU"
else: 
    print(TerminalColor.SUCESS+"Concenssão de Permissão realizada com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nConcenssão de Permissão realizada com SUCESSO"


sleep(1)


def clicando_permissao_location_all_time(webdriver):
    allowAllTheTime = webdriver.find_element_by_xpath("//android.widget.Button[@text='Allow all the time']")
    return bool (clicando_permissao_location_all_time)

espera.until(clicando_permissao_location_all_time)
try:
   allowAllTheTime = driver.find_element_by_xpath("//android.widget.Button[@text='Allow all the time']").click()
except: 
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar conceder permissão para uso da localização o tempo todo - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar conceder permissão para uso da localização o tempo todo - FALHOU"
else:
    print(TerminalColor.SUCESS+"Concessão de permissão realizada com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nConcessão de permissão realizada com SUCESSO"



def clicando_exibindo_producao_diaria(webdriver):
    producaoDiaria = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[3]/android.view.View[1]")
    return bool (producaoDiaria)

espera.until(clicando_exibindo_producao_diaria)
try:
    producaoDiaria = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[3]/android.view.View[1]").click()
except:
    print(TerminalColor.ERRO+"ERRO - Não foi possível localizar e exibir o menu de produção diária - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Não foi possível localizar e exibir o menu de produção diária - FALHOU"
else:
    print(TerminalColor.SUCESS+"SUCESSO ao localizar e exibir menu de produção diária"+TerminalColor.NORMAL)
    textRelatorio += "\nSUCESSO ao localizar e exibir menu de produção diária"


with open("Relatório_Driver_12.txt", 'w') as arquivo:
    arquivo.write(textRelatorio)

