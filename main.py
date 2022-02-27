
from appium.webdriver import Remote
from Passageiro.testeDeLogin.testeLogin import TesteLogin

class Main():
    
    def driver(args):      
        driver =  Remote(
                    'http://127.0.0.1:4723/wd/hub',
                    {
                    'platformName': 'Android',
                    'appium:deviceName': 'AppiumP',
                    'appium:app': args['url'] ,
                    'appium:avd': 'Nexus_4_API_28',
                    'isHeadless' : True,
                    'avdArgs': "-no-window"
                    })
                
            
        return driver
    
if __name__ == '__main__':
    TesteLogin.criando_teste_login