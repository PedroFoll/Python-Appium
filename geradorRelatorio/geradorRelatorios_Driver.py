
import os
from helpers.helpers import Helpers




class GerandoRelatorio():

    def gerando_pasta_relatorio(driver, dados, textRelatorio):
        
        nomeRelatorio = dados['nome_relatorio']
        nomeApp = dados['nomeApp']
        tipoPlataforma = dados['tipo_plataforma']
        dataTime = Helpers.gerador_data_hora()
        name = driver.current_activity
        namePrint = name+dataTime
        

        htmlHead = '<!DOCTYPE html><html lang="bt-BR"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Relatório Teste</title><h1>Teste de Relatório</h1><h3>Itens testados</h3><ul>'
        htmlFoot = '</ul></body></html>'
        imagemRelatorio = '<p><img src="relatorios/'+namePrint+'.png alt="some text" width=320 height=618></p>'


        if os.path.isdir("relatorios/"+nomeApp): # vemos de este diretorio ja existe
            os.mkdir("relatorios/"+nomeApp+"/"+nomeRelatorio+" "+dataTime)
            driver.save_screenshot("relatorios/"+nomeApp+"/"+namePrint+".png")
            with open("relatorios/"+nomeApp+"/"+nomeRelatorio+" "+dataTime+"/TESTE_DE_"+ nomeRelatorio +".html", 'w') as arquivo:
                arquivo.write("Teste realizado\n"+dataTime+"\n")
                arquivo.write(htmlHead+textRelatorio+imagemRelatorio+htmlFoot)
            return 'Já existe'
        else:
            os.mkdir("relatorios/"+nomeApp+"/"+nomeRelatorio+" "+dataTime) # aqui criamos a pasta caso nao exista
            with open("relatorios/"+nomeApp+"/"+nomeRelatorio+" "+dataTime+"/TESTE_DE_"+ nomeRelatorio +".html", 'w') as arquivo:
                arquivo.write("Teste realizado\n"+dataTime+"\n")
                arquivo.write(htmlHead+textRelatorio+imagemRelatorio+htmlFoot)
                return 'Pasta criada com sucesso!'