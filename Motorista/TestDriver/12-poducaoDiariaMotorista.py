
from appium.webdriver import Remote
from functionsDriver12 import*


driver = Remote(
    'http://127.0.0.1:4723/wd/hub',
    {
    'platformName': 'Android',
    'appium:deviceName': 'AppiumP',
    'appium:app': '/home/ulisses/Projetos/Estudos/testemobile/app-test.apk',
    'appium:avd': 'Pixel_5_API_29'
    }
    )


selecionar_opcao_login

preencher_campo_login

selecionar_campo_senha

clicando_botao_logar

aceitando_permissao_localizacao

Permissao_Local

aceitando_permissao_localizacao

clicando_permissao_location_all_time

clicando_exibindo_producao_diaria