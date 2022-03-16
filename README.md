# Automation704_Flask

Projeto de automação de testes com Appium, construído com Python-Client, executado através de Servidor web com Flask

## IMPORTANTE - Itens essenciais para o ambiente de desenvolvimento de testes!!

É necessário configurar o ambiente com os seguintes programas:

1 - JDK v8 (sudo apt install openjdk-8-jdk)

2 - ADB TOOLS (sudo apt install android-tools-adb)

3 - ANDROID STUDIO (sudo apt install snapd && sudo snap install android-studio --classic)

4 - APPIUM (npm install -g appium)
    OBS: Necessário instalar nvm e nvm versão v12.22.8

5 - Configuração das Variáveis de Ambiente (atenção para a localização dos diretórios)
        No terminal: "nano ~/.bashrc"
    {
        export ANDROID_HOME="$HOME/Android/Sdk"
        export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
        export ABD="$ANDROID_HOME/platform-tools/adb"
    }
        NÃO ESQUECER de rodar o comando "source ~/.bashrc"

6 - APPIUM DOCTOR (npm install appium-doctor -g)
        No terminal: "appium-doctor"
        Se tudo estiver OK, já será possível clonar os projetos e começar a codar.


# Python-Appium - Windows
  
 00- Para executar os testes, são necessários :
  Emulação de alguma versão do andoid que tenha webViwer (Recomenda-se o uso do Nexus 5, na configuração "maindriver.py" é feito o envio do remotedriver para a comunicação com o emulador, e o emulador que tem lá é o "Nexus_5_API_29" que foi utilizado para o desenvolvimento da automação.
    
    JDK 1.8 ; 
    Appium versão maior que 1.7.2;
    Android Studio; 
    ADB Devices;
    ADB manager (instalado pelo Android studio); 
    Appium doctor- (Opcional).
   
01 - Baixar. instalar e configurar o Appium - https://github.com/appium/appium-desktop/releases/tag/v1.22.2

02 - Configurar o Android_home: CONFIGURAR O ANDROID HOME NO WINDOWS PARA O APPIUM - YouTube - https://www.youtube.com/watch?v=yuKlc-a5z5k&ab_channel=qazando

03 - Configurar o Java_home: Configurando variáveis de ambiente Java no Windows 10 - YouTube - https://www.youtube.com/watch?v=qo6KKuc5gho&ab_channel=JorgeLuisBoeiraBavaresco

04 - Configurar o Path do appium. (Somente para utliza-lo pelo CMD não existe necessidade real dessa configuração)

05 - Necessario a instalação, para visualização dos elementos da tela, um inspetor de elementos
     podem ser utilizado: 
     
     "UIAutomatorViewer - Incluso no Android Studio - Path = \AppData\Local\Android\Sdk\tools\bin"
     "AppiumInspector - https://github.com/appium/appium-inspector/releases"
     