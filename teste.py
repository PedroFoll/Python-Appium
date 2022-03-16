
from datetime import datetime
import config
from models.relatorio import Relatorio

dados = ['teste Relatorio', 'hml', 'android', datetime.now(), 'abcdefgh', 'finalizado', 'FALSE']

teste01 = Relatorio('teste Relatorio', 'hml', 'android', datetime.now(), 'abcdefgh', 'finalizado', 'FALSE')

config.session.add(teste01)

config.session.commit()