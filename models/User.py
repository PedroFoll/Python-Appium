from teste_envio_relatorio import Envio_relatorio

if __name__ == '__main__':
    peter = Envio_relatorio.query.filter_by(nomeApp='fabricahmls').first()
    print( peter.nome_do_app)


