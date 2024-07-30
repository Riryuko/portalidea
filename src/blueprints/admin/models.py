"""Tabela de alunos"""

import random
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def gerar_senha_aletoria():
    """Cria uma senha de 6 digitos"""
    return str(random.randint(100000, 999999))

class Alunos(Base):
    """Tabela alunos"""

    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telefone = Column(String(20), nullable=True)
    senha = Column(String(6), default=gerar_senha_aletoria, nullable=False)
