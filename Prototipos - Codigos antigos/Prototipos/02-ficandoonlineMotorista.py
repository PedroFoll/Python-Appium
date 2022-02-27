from sys import platform
import unittest
from time import sleep
from appium.webdriver import Remote
from appium.webdriver.extensions.search_context import android
driver= Remote( 
        'http://localhost:4723/wd/hub',
{
  "platformName": "android",
  "appium:deviceName": "AppiumP",
  "appium:avd": "Pixel_5_API_29",
  "appium:app": "C:/Users/pedro/Documents/Projetos Python-Appium/app-test.apk"
}
)

#Ficando online pela primeira vez (Descobrir forma de fazer um "IF" para pular ou não essa etapa)
#Todo os Xpaths que serão utilizados como variaveis
aceptlocation = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[26]/android.view.View/android.widget.ListView/android.view.View[2]")
devicelocation = ("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")
devicemidia = ("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")
negativemoney = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.app.Dialog/android.view.View[3]/android.view.View/android.widget.Button")

#Començando os comandos das variaveis
clickAceptLocation=driver.find_element_by_xpath(aceptlocation)
clickAceptLocation.click()

clickdeviceLocation=driver.find_element_by_xpath(devicelocation)
clickdeviceLocation.click()

clickdeviceMidia=driver.find_element_by_xpath(devicemidia)
clickdeviceMidia.click()
