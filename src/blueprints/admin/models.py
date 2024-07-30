"""Fila de Motoristas"""



from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from src.database import Base


class DriverQueue(Base):
    """Motorist Queue"""

    __tablename__ = "driver_queue"
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    telefone = Column(String(15))
    bairro = Column(String(255))
    date_time = Column(DateTime(), default=datetime.now)
