# pylint: disable=too-few-public-methods, consider-using-f-string
"""User Querys"""

from src.database.db_connection import db_connector
from .models import Alunos

class AlunosQuerys:
    """Gerencia a tabela de alunos - CRUD"""

    @classmethod
    @db_connector
    def criar(cls, connection, nome, email, telefone):
        """Cria uma matricula nova"""
        checar_email = connection.session.query(Alunos).filter_by(email=email).first()
        if checar_email == None:
            aluno = Alunos(nome=nome, email=email, telefone=telefone)
            connection.session.add(aluno)
            connection.session.commit()
        return None

    @classmethod
    @db_connector
    def atualizar(cls, connection, aluno_id, nome=None, email=None, telefone=None):
        """Atualiza os dados do aluno"""
        return None

    @classmethod
    @db_connector
    def deletar(cls, connection, aluno_id):
        """Deleta os dados do aluno"""
        aluno = connection.session.query(Alunos).filter_by(id=aluno_id).first()
        if aluno:
            connection.session.delete(aluno)
            connection.session.commit()
            return "Aluno deletado com sucesso."
        else:
            return "Aluno não encontrado."