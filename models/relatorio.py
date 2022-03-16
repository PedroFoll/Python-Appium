
from sqlalchemy import Column, VARCHAR, DateTime, Integer
import config


class Relatorio(config.base):
    __tablename__ = 'relatorio'
    id = Column(Integer, primary_key=True)
    nome_relatorio = Column(VARCHAR(45))
    nome_app = Column(VARCHAR(45))
    tipo_plataforma = Column(VARCHAR(45))
    data_hora = Column(DateTime(6))
    imagem = Column(VARCHAR(255))
    status = Column(VARCHAR(45))
    erro = Column(VARCHAR(45))
    
    def __init__(self, nome_relatorio, nome_app, tipo_plataforma, data_hora, imagem, status, erro):
        self.nome_relatorio = nome_relatorio
        self.nome_app = nome_app
        self.tipo_plataforma = tipo_plataforma
        self.data_hora = data_hora
        self.imagem = imagem
        self.status = status
        self.erro = erro

