from genericpath import exists
from automation704_flask.geradorRelatorio.geradorRelatorios_Driver import GerandoRelatorio
from setup import db

class Model(db.Models):

    __name__       = 'tbRelatorios'

    id             = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name_report    = db.Column(db.String(100))
    name_app       = db.Column(db.String(30))
    test_type      = db.Column(db.String(50))
    plataform_type = db.Column(db.String(20))
    date_time      = db.Column(db.Date())
    link_image     = db.Column(db.String(100))
    msg_error      = db.Column(db.String(100))
    status         = db.Column(db.String(20))


    def __init__(self, name_report, name_app, test_type, plataform_type, date_time, link_image, msg_error, status):
        self.name_report    = name_report
        self.name_app       = name_app
        self.test_type      = test_type
        self.plataform_type = plataform_type
        self.date_time      = date_time
        self.link_image     = link_image
        self.msg_error      = msg_error
        self.status         = status


    def create_table():
        db.create()
        db.commit()

    
    def add_report(dados, self):
        if exists.__name__ == "tbRelatorios":
            db.add(dados)
        else:
            db.create()
            db.add(dados)
        db.commit()


