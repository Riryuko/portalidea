# pylint: disable=too-few-public-methods, consider-using-f-string
"""User Querys"""

from src.database.db_connection import db_connector
from .models import DriverQueue

class BotQuerys:
    """A Consult if name alredy exits"""
    @classmethod
    @db_connector
    def fila(cls, connection):
        """Return all motorists in database"""
        return connection.session.query(DriverQueue).all()

    @classmethod
    @db_connector
    def novo(cls, connection, name, telefone, bairro):
        """someting"""
        check_name = connection.session.query(DriverQueue).filter_by(name=name).first()
        if check_name == None:  # pylint: disable=singleton-comparison
            new = DriverQueue(name=name, telefone=telefone, bairro=bairro)
            connection.session.add(new)
            connection.session.commit()

    @classmethod
    @db_connector
    def remove_first_driver(cls, connection, telefone):
        """Remove the first driver in the queue and return its data"""
        first_driver = connection.session.query(DriverQueue).filter_by(telefone=telefone).first()
        if first_driver:
            first_driver_data = {
                'name': first_driver.name,
                'telefone': first_driver.telefone,
                'bairro': first_driver.bairro
            }
            connection.session.delete(first_driver)
            connection.session.commit()
            return first_driver_data
        else:
            return None

    @classmethod
    @db_connector
    def sair_da_fila(cls, connection, telefone):
        """someting"""
        check_name = connection.session.query(DriverQueue).filter_by(telefone=telefone).first()
        if check_name != None:  # pylint: disable=singleton-comparison
            connection.session.delete(check_name)
            connection.session.commit()