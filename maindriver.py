from appium.webdriver import Remote

class Driver():
    
    def driver(args):      
        driver=Remote(
                    'http://localhost:4723/wd/hub',
                    {
                    "platformName": "android",
                    "appium:deviceName": "AppiumP",
                    "appium:app": args['url'],
                    "appium:avd": "Nexus_5_API_29",
                    
                    })
    
        return driver

