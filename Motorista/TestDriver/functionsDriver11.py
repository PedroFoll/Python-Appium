
from appium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
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

sleep(4)

#CLICANDO NO BOTÂO INICIAR/START
TouchAction(driver).tap(x=540, y=1792).perform()

sleep(8)

#PERMITINDO SOBREPOSIÇÂO DO APP SOB OUTROS APPS
'''
def clicando_switch_permissao_sobreposicao(webdriver):
    botaoSwitchPermissao = webdriver.find_element_by_xpath("//android.widget.Switch[@recource-id='android:id/switch_widget']")
    return bool (botaoSwitchPermissao)

espera.until(clicando_switch_permissao_sobreposicao)
try:
    botaoSwitchPermissao = driver.find_element_by_xpath("//android.widget.Switch[@recource-id='android:id/switch_widget']").click()
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar acionar swith de permissão - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "ERRO - Falha ao tentar acionar swith de permissão - FALHOU"
else:
    print(TerminalColor.SUCESS+"Permissão de sobreposição acionada com SUCESSO"+TerminalColor.NOMRAL)
    textRelatorio += "Permissão de sobreposição acionada com SUCESSO"
'''

#ACESSANDO MENU

TouchAction(driver).tap(x=970, y=206).perform()
sleep(5)
def clicando_menu_perfil_motorista(webdriver):
    profileButton = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View")
    return bool (profileButton)

espera.until(clicando_menu_perfil_motorista)
try:
    profileButton = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View").click()
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar localizar e acionar MENU PERFIL - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar localizar e acionar MENU PERFIL - FALHOU"
else:
    print(TerminalColor.SUCESS+"MENU PERFIL localizado e acessado com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nMENU PERFIL localizado e acessado com SUCESSO"


sleep(1)


def selecionando_opcao_veiculo(webdriver):
    botaoVeiculo = webdriver.find_element_by_xpath("//android.view.View[@resource-id='vehicleDriver']")
    return bool (botaoVeiculo)

espera.until(selecionando_opcao_veiculo)
try:
    botaoVeiculo = driver.find_element_by_xpath("//android.view.View[@resource-id='vehicleDriver']").click()
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar localizar e selecionar opção VEÍCULO - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar localizar e selecionar opção VEÍCULO - FALHOU"
else:
    print(TerminalColor.SUCESS+"Seleção da opção VEÍCULO realizado com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nSeleção da opção VEÍCULO realizado com SUCESSO"


sleep(1)


def selecionando_requisicao_troca_veiculo(webdriver):
    trocarVeiculo = webdriver.find_element_by_xpath("//android.view.View[@resource-id='btnRequestChangeVehicle']")
    return bool (trocarVeiculo)

espera.until(selecionando_requisicao_troca_veiculo)
try:
    trocarVeiculo = driver.find_element_by_xpath("//android.view.View[@resource-id='btnRequestChangeVehicle']").click()
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar realizar requisição de troca de VEÍCULO - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar realizar requisição de troca de VEÍCULO - FALHOU"
else:
    print(TerminalColor.SUCESS+"Seleção de opção Requisição de troca de Veículo realizada com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nSeleção de opção Requisição de troca de Veículo realizada com SUCESSO"


## AÇÕES DE PREENCHIMENTO DE INFORMAÇÔES DO NOVO VEÌCULO

def preenchendo_informacoes_novo_veiculo(webdriver):
    novaMarca = webdriver.find_element_by_xpath("//android.widget.EditText[@resource-id='brandDriverEdit']")
    return bool (novaMarca)

espera.until(preenchendo_informacoes_novo_veiculo)
try:
    novaMarca = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='brandDriverEdit']").send_keys("CARRO1000")
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar preencher o campo MARCA - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar preencher o campo MARCA - FALHOU"
else:
    print(TerminalColor.SUCESS+"NOVA MARCA preenchida com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nNOVA MARCA preenchida com SUCESSO"


try:
    novoModelo = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='modelDriverEdit']").send_keys("MOTOR1000")
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar preencher o campo MODELO - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar preencher o campo MODELO - FALHOU"
else:
    print(TerminalColor.SUCESS+"NOVO MODELO preenchido com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nNOVO MODELO preenchido com SUCESSO"


try:
    novaPlaca = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='plateLicenseEdit']").send_keys("TST-1234")
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar preencher o campo PLACA - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar preencher o campo PLACA - FALHOU"
else:
    print(TerminalColor.SUCESS+"NOVA PLACA preenchido com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nNOVA PLACA preenchido com SUCESSO"


try:
    novoAnoFabricacao = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='yearLicenseEdit']").send_keys("2022")
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar preencher o campo ANO DE FABRICAÇÃO- FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar preencher o campo ANO DE FABRICAÇÃO- FALHOU"
else:
    print(TerminalColor.SUCESS+"NOVO ANO DE FABRICAÇÃO preenchido com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nNOVO ANO DE FABRICAÇÃO preenchido com SUCESSO"


try:
    novaCor = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='colorLicenseEdit']").send_keys("Preta")
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar preencher o campo COR DO VEÍCULO- FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar preencher o campo COR DO VEÍCULO- FALHOU"
else:    
    print(TerminalColor.SUCESS+"NOVA COR DO VEÍCULO preenchida com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nNOVA COR DO VEÍCULO preenchida com SUCESSO"


try:
    novoRenavam = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='renavamLicenseEdit']").send_keys("123456789")
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar preencher o campo RENAVAM - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar preencher o campo RENAVAM - FALHOU"
else:
    print(TerminalColor.SUCESS+"NOVO RENAVAM preenchido com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nNOVO RENAVAM preenchido com SUCESSO"



def clicando_botao_enviar(webdriver):
    botaoEnviarNewVehicle = webdriver.find_element_by_xpath("//android.widget.Button[@resource-id='btnSaveCarInsert']")
    return bool (botaoEnviarNewVehicle)

espera.until(clicando_botao_enviar)
try:
    botaoEnviarNewVehicle = driver.find_element_by_xpath("//android.widget.Button[@resource-id='btnSaveCarInsert']").click()
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar clicar no Botão ENVIAR - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar clicar no Botão ENVIAR - FALHOU"
else:
    print(TerminalColor.SUCESS+"CLIQUE no botão ENVIAR realizado com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nCLIQUE no botão ENVIAR realizado com SUCESSO"



def certificando_solicitacao_troca_veiculo(webdriver):
    botaoOkCertificandoSolicitacaoTrocaVeiculo = webdriver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.app.Dialog/android.view.View[3]/android.view.View/android.widget.Button")
    return bool (botaoOkCertificandoSolicitacaoTrocaVeiculo)

espera.until(certificando_solicitacao_troca_veiculo)
try:
    botaoOkCertificandoSolicitacaoTrocaVeiculo = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.app.Dialog/android.view.View[3]/android.view.View/android.widget.Button").click() 
except:
    print(TerminalColor.ERRO+"ERRO - Falha ao tentar clicar na opção OK para certificar solicitação de TROCA DE VEÍCULO - FALHOU"+TerminalColor.NORMAL)
    textRelatorio += "\nERRO - Falha ao tentar clicar na opção OK para certificar solicitação de TROCA DE VEÍCULO - FALHOU"
else:
    print(TerminalColor.SUCESS+"CLIQUE no BOTÃO OK realizado com SUCESSO"+TerminalColor.NORMAL)
    textRelatorio += "\nCLIQUE no BOTÃO OK realizado com SUCESSO"


##GERADOR DO RELATÓRIO
with open("Relatório_Driver_11.txt", "w") as arquivo:
    arquivo.write(textRelatorio)
    