
from re import T
from flask import Flask, request
from Motorista.aceitar_corrida_agendada.aceitando_corrida_agendada import Aceitar_Agendamento
from Motorista.cancelar_agendamento.cancelar_agendamento import Cancelar_agendamento
from Motorista.mudar_foto_motorista.mudar_foto import Mudar_Foto
from Motorista.mudar_senha_motorista.mudar_senha import Trocando_senha
from Passageiro.testeAddMotoristaFavorito.testeAddMotoristaFavorito import TesteAddMotoristaFavorito
from Passageiro.testeDeCadastro.testeCadastro import TesteCadastroClient
from Passageiro.testeDeLogin.testeLogin import TesteLoginClient
from Passageiro.testeMudarFoto.testeMudarFoto import TesteMudarFotoClient
from Passageiro.testeMudarSenha.testeMudarSenha import TesteMudarSenhaClient
from Passageiro.testeChamado.testeChamado import TesteChamado
from Motorista.teste_login.testes_loginM import Teste_Login
from Motorista.teste_cadastro.teste_Cadastro_Motorista import Teste_Cadastro_Motorista
from setup import db

#myslq://root:root@localhost/flasksql

app = db.app

@app.route('/teste-login', methods=['POST'])
def teste_login():
    request_data = request.get_json()
    return TesteLoginClient.criando_teste_login(request_data)


@app.route('/teste-chamado', methods=['POST'])
def teste_chamado():
    request_data = request.get_json()
    return TesteChamado.criando_teste_chamado(request_data)

##########################################################################################################

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

###########################################################################################################

@app.route ('/teste-cadastro', methods=['POST'])
def teste_cadastro():
    request_data = request.get_json()
    return TesteCadastroClient.criando_teste_cadastro_passageiro(request_data)


@app.route ('/teste-mudar-senha-cliente', methods=['POST'])
def teste_mudar_senha_cliente():
    request_data = request.get_json()
    return TesteMudarSenhaClient.criando_teste_mudar_senha_passageiro(request_data)


@app.route ('/teste-mudar-foto-cliente', methods=['POST'])
def teste_mudar_foto_cliente():
    request_data = request.get_json()
    return TesteMudarFotoClient.criando_teste_mudar_foto_passageiro(request_data)


@app.route ('/teste-add-motorista-favorito', methods=['POST'])
def teste_add_motorista_favorito():
    request_data = request.get_json()
    return TesteAddMotoristaFavorito.criando_teste_add_motorista_favorito(request_data)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = "159753"
    db.init_app(app)
    app.run(debug = True)