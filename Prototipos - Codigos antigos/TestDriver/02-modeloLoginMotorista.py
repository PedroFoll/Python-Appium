
from functionsDriver02 import*
from appium.webdriver import Remote


driver = Remote(
    'http://127.0.0.1:4723/wd/hub',
    {
    'platformName': 'Android',
    'appium:deviceName': 'AppiumP',
    'appium:app': '/home/ulisses/Projetos/Estudos/testemobile/app-test.apk',
    'appium:avd': 'Pixel_5_API_29'
    }
    )

#início - selecionando opção inicial
selecionar_opcao_login


#preenchendo login
preencher_campo_login


#preencher senha
selecionar_campo_senha


#logando
clicando_botao_logar