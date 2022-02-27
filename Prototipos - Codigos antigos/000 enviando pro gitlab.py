class TerminalColor:
    ASSERT = '\033[32m' #Verde
    ERRO = '\033[91m' #Vermelho
    NORMAL = '\033[0m' #Branco
varRandom = "Teste"

print(TerminalColor.ASSERT +'='*26+'\nFuncoinando \n'+'='*26+TerminalColor.NORMAL)
try:
    print()
except:
    print(TerminalColor.ERRO+'='*40+"\n \n"+'='*40+TerminalColor.NORMAL)
    varRandom +="\n"
else:
    print(TerminalColor.SUCCESS+" "+TerminalColor.NORMAL)
    varRandom +="\n"
    
with open("RelatorioModelo.txt", 'w') as arquivo:
    arquivo.write("textRelatorio")

##############################################################################################
############################SCRIPT FINALIZADO#################################################
##############################################################################################