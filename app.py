from flask import Flask, request
from Motorista.iniciar_macaneta_manual.macaneta_motorista import Macaneta_manual
from Motorista.aceitar_corrida_agendada.aceitando_corrida_agendada import Aceitar_Agendamento
from Motorista.cancelar_agendamento.cancelar_agendamento import Cancelar_agendamento
from Motorista.enviando_mensagens.enviar_mensagens import Enviar_mensagem
from Motorista.mudar_foto_motorista.mudar_foto import Mudar_Foto
from Motorista.mudar_senha_motorista.mudar_senha import Trocando_senha
from Motorista.teste_login.testes_loginM import Teste_Login
from Motorista.teste_cadastro.teste_Cadastro_Motorista import Teste_Cadastro_Motorista
from Motorista.liberacao_corrida.liberar_corrida import Liberar_corrida
from Motorista.aceitando_corridas.aceitar_corrida import Aceitar_corrida
from Motorista.finalizando_chamado.finalizar_chamado import Finalizar_chamado


app = Flask(__name__)

##########################################################################################################
@app.route('/macaneta_manual',methods=["POST"])
def Macaneta():
    req=request.get_json()
    return Macaneta_manual.Iniciando_macaneta(req)
    

@app.route('/teste_login_Motorista', methods=["POST"])
def Teste_login():
    req = request.get_json()
    return Teste_Login.Logando_Motorista(req)
    

@app.route('/teste_cadastro_Motorista', methods=["POST"])
def Teste_Cadastro_motorista():
    req = request.get_json()
    return Teste_Cadastro_Motorista.Cadastrando_Motorista(req) 


@app.route('/mudar_senha_motorista', methods=['POST'])
def mudar_senha_motorista():
    req = request.get_json()
    return Trocando_senha.troca_senha(req)

@app.route('/mudar_foto_motorista', methods=['POST'])
def mudar_foto_motorista():
    req = request.get_json()
    return Mudar_Foto.mudando_foto(req)

@app.route('/aceitar_corrida_agendada', methods=['POST'])
def aceite_agendamento():
    req = request.get_json()
    return Aceitar_Agendamento.aceitando_corrida(req)

@app.route('/cancelar_agendamento', methods=['POST'])
def cancelar_agendamento():
    req = request.get_json()
    return Cancelar_agendamento.cancelando_corrida_agendada(req)

@app.route('/liberar_corrida',methods=['POST'])
def liberando_corrida():
    req = request.get_json()
    return Liberar_corrida.liberando_corrida(req)

@app.route('/aceitar_corrida',methods=['POST'])
def aceitando_corridas():
    req = request.get_json()
    return Aceitar_corrida.aceitando_corridas(req)

@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    req = request.get_json()
    return Enviar_mensagem.enviando_mensagem(req)

@app.route('/finalizar_corrida',methods=['POST'])
def finalizar_corridas():
    req = request.get_json()
    return Finalizar_chamado.finalizando_chamado(req)



if __name__ == '__main__':
    app.run(debug = True)