from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/FlaskDB'
                                    #Banco://Usuario:senha@porta:YYYY/NomeDoBanco
db=SQLAlchemy(app)

