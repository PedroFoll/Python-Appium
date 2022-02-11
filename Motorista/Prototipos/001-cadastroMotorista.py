from variaveisCadastro import*
from gerador_cpf import cpf_validado
from gerador_telefone import numeroCelularAleatorio
import random
import random
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from Z0Cadastro_functions import*


#Inicio do relatorio
appName='Fabrica Homologacao.html'
f1=open("C:/Users/pedro/Documents/testemobile/Relatorios/"+appName,'wt')
f1.write("<h1><strong>Relatorio de testes</strong></h1>\n<h3><p>Teste de cadastro</h3></p>\n<hr>")
#Desire Cap 
#função para gerar email aleatorio
inicio=(str('motoristateste'))
final=(str('@teste.com'))
meio=(str(random.randint(1,99999)))
randoMail=(inicio+meio+final)
#Entrando no cadastro de motorista
botaoRegister = driver.find_element_by_xpath(register)
botaoRegister.click()
sleep(6)

#Selecionando tipo de motorista
driverTypeButton = driver.find_element_by_xpath(clickDriverType)
driverTypeButton.click()
sleep(6)

#Digitando o Nome
nameField = driver.find_element_by_xpath(toTypeName)
nameField.click()
nameField.send_keys("Homologação Fb704")
sleep(1)

#Utilizando o botão de next
nextButton01=driver.find_element_by_xpath(nextButton00)
nextButton01.click()
sleep(1)

#Digitando o CPf
cpfField= driver.find_element_by_xpath(toTypeCpf)
cpfField.send_keys(cpf_validado)
cpfField.click()
nextButton01.click()
sleep(3)

try: 
  clickOkButtonCpf=driver.find_element_by_xpath(okButtonCpf)
  clickOkButtonCpf.click()
except:
  f2=open("C:/Users/pedro/Documents/testemobile/Relatorios/"+appName,'at')
  f2.write('\n<br> O CPF nao esta sendo utilizado<br>') 
else:
  f2=open("C:/Users/pedro/Documents/testemobile/Relatorios/"+appName,'at')
  f2.write("\n<br> O CPF cadastrado ja esta sendo utilizado<br>")
 
#Digitando o Email
emailField= driver.find_element_by_xpath(toTypeEmail)
emailField.send_keys(randoMail)
sleep(1)
nextButton01.click()

#Digitando o Telefone
numberField= driver.find_element_by_xpath(toTypePhone)
numberField.send_keys(numeroCelularAleatorio)
sleep(1)

#DropDown Button
genderField1= driver.find_element_by_xpath(toSetGender1)
genderField1.click()
sleep(5)
genderField2 = driver.find_element_by_xpath(toSetGender2)
genderField2.click()

#Botão de Next
nextButton= driver.find_element_by_xpath(toContinue)
nextButton.click()
sleep(6)
#Situações de erro (Email ou cpf invalidos)
if erroMsgEmail is True:
  f3=open("C:/Users/pedro/Documents/testemobile/Relatorios/"+appName,'at')
  f3.write("\n<br> O Email utilizado ja esta cadastrado<br>")
  clickOkButtonEmail=driver.find_element_by_xpath(okButtonEmail)
  clickOkButtonEmail.click()
else:
  f3=open("C:/Users/pedro/Documents/testemobile/Relatorios/"+appName,'at')
  f3.write("\n<br> O email nao esta sendo utilizado<br>") 

#Inserindo senha
passWordField=driver.find_element_by_xpath(toTypePassword)
passWordField.click()
passWordField.send_keys("123456")
sleep(3)
confirmPassWordField=driver.find_element_by_xpath(toConfirmPassword)
confirmPassWordField.click()
confirmPassWordField.send_keys("123456")
sleep(3)
nextButton= driver.find_element_by_xpath(toContinue)
nextButton.click()
sleep(3)

#Selecionando estado/pais/cidade
selectCity1=driver.find_element_by_xpath(citySelector1)
selectCity1.click()
sleep(2)
selectCity2=driver.find_element_by_xpath(citySelector2)
selectCity2.click()
sleep(2)
nextButton= driver.find_element_by_xpath(toContinue)
nextButton.click()

#Ação para mover para cima na parte dos termos de uso e aceitar os termos
actions = TouchAction(driver)
actions.press(x=48, y=1909)
actions.move_to(x=52, y=1194)
actions.release() 
actions.perform()
sleep(1)
checkBoxTermos=driver.find_element_by_xpath(useTerms)
checkBoxTermos.click()
sleep(1)
nextButton= driver.find_element_by_xpath(toContinue)
nextButton.click()
sleep(3)

#Batendo a foto pelo emulador/celular conectado para o cadastro de perfil
openCamera=driver.find_element_by_xpath(toAcessCamera)
openCamera.click()
""" aceptCameraAllow=driver.find_element_by_xpath(allowCamera)
aceptCameraAllow.click() """
sleep(3)
takeFoto=driver.find_element_by_accessibility_id("Shutter")
takeFoto.click()
sleep(3)
sendFoto= driver.find_element_by_accessibility_id("Done")
sendFoto.click()
sleep(3)
nextButton= driver.find_element_by_xpath(toContinue)
nextButton.click()
sleep(3)

#Inserindo dados do carro
toTypeVehicleBrand=driver.find_element_by_xpath(vehicleBrand)
toTypeVehicleBrand.send_keys('Fiat')
toTypeVehicleModel=driver.find_element_by_xpath(vehicleModel)
toTypeVehicleModel.send_keys('Uno')
toTypeVehiclePlate=driver.find_element_by_xpath(vehiclePlate)
toTypeVehiclePlate.send_keys('TST-0704')
toTypeVehicleVinNumber=driver.find_element_by_xpath(vehicleVinNumber)
toTypeVehicleVinNumber.send_keys('12171174856') #Não sei a formatação do renavam
toTypeVehicleColor=driver.find_element_by_xpath(vehicleColor)
toTypeVehicleColor.send_keys('Azul')
toTypeSeatsNumber=driver.find_element_by_xpath(vehicleSeatsNumber)
toTypeSeatsNumber.send_keys('5')
toTypeVehicleYear=driver.find_element_by_xpath(vehicleYear)
toTypeVehicleYear.send_keys('2018')
nextButton= driver.find_element_by_xpath(toContinue)
nextButton.click()
sleep(3)

#Campos das documentações do motorista. 
#CNH
toTypeCnh=driver.find_element_by_xpath(toTypeCnhField)
toTypeCnh.send_keys("69432109613")
sleep(3)
cnhFoto= driver.find_element_by_xpath(documentsSendFotos)
cnhFoto.click()
sleep(3)
selectCamera= driver.find_element_by_id("android:id/button2")
selectCamera.click()
sleep(3)
takeFoto=driver.find_element_by_accessibility_id("Shutter")
takeFoto.click()
sleep(3)
sendFoto= driver.find_element_by_accessibility_id("Done")
sendFoto.click()
sleep(3)
nextButtonDocuments= driver.find_element_by_xpath(toContinueButtonDocuments)
nextButtonDocuments.click()
sleep(3)

#CRLV
toTypeCrlv=driver.find_element_by_xpath(toTypeCrlvField)
toTypeCrlv.send_keys('Teste fabrica 704')
clrvFoto= driver.find_element_by_xpath(documentsSendFotos)
clrvFoto.click()
sleep(3)
selectCamera= driver.find_element_by_id("android:id/button2")
selectCamera.click()
sleep(3)
takeFoto=driver.find_element_by_accessibility_id("Shutter")
takeFoto.click()
sleep(3)
sendFoto= driver.find_element_by_accessibility_id("Done")
sendFoto.click()
sleep(3)
nextButtonDocuments= driver.find_element_by_xpath(toContinueButtonDocuments)
nextButtonDocuments.click()
sleep(3)

#Atecedentes criminais
toTypeCriminalPast=driver.find_element_by_xpath(toTypeCriminalPastField)
toTypeCriminalPast.send_keys('Teste fabrica 704')
criminalPastFoto= driver.find_element_by_xpath(documentsSendFotos)
criminalPastFoto.click()
sleep(3)
selectCamera= driver.find_element_by_id("android:id/button2")
selectCamera.click()
sleep(3)
takeFoto=driver.find_element_by_accessibility_id("Shutter")
takeFoto.click()
sleep(3)
sendFoto= driver.find_element_by_accessibility_id("Done")
sendFoto.click()
sleep(3)
nextButtonDocuments= driver.find_element_by_xpath(toContinueButtonDocuments)
nextButtonDocuments.click()
sleep(5)

#antecedentes criminais
clickProofOfAddress=driver.find_element_by_xpath(proofOfAddress)
clickProofOfAddress.click()
sleep(3)
selectCamera= driver.find_element_by_id("android:id/button2")
selectCamera.click()
sleep(3)
takeFoto=driver.find_element_by_accessibility_id("Shutter")
takeFoto.click()
sleep(3)
sendFoto= driver.find_element_by_accessibility_id("Done")
sendFoto.click()
sleep(3)
nextButtonDocuments= driver.find_element_by_xpath(toContinueButtonDocuments)
nextButtonDocuments.click()
sleep(10)

#Finalizando o cadastro
try:
  finalButton=driver.find_element_by_xpath(lastNextButton)
  finalButton.click()
except:
  f4=open("C:/Users/pedro/Documents/testemobile/Relatorios/"+appName,'at')
  f4.write("\n<br> O Cadastro foi nao pode ser concluido com sucesso<br>")
else:
  f4=open("C:/Users/pedro/Documents/testemobile/Relatorios/"+appName,'at')
  f4.write("\n<br> O Cadastro foi concluido com sucesso<br>")

#Fim do cadastro