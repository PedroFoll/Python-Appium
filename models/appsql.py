from flask import Flask, Response, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'FlaskDB'

mysql = MySQL(app)


@app.route('/Teste_sql', methods = ['POST'])
def index():
    details = request.get_json()
    nomedoapp = details['nome_do_app']
    tipodeteste = details['tipo_de_teste']
    plataforma = details['plataforma']
    status = details['status']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user(nome_do_app, tipo_de_teste, plataforma, status) VALUES(%s, %s, %s, %s)",(nomedoapp, tipodeteste, plataforma,status))
    mysql.connection.commit()
    cur.close()
    return 'sucess'


if __name__ == '__main__':
    app.run(debug = True)