from sqlalchemy import Column, String, Integer, Double
from conexao import db

class Aluno (db.Model):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome =Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String)
    telefone= Column(String)
    cep = Column(String)
    estado = Column(String)
    cidade = Column(String)
    funcao = Column(String)