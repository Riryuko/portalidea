# pylint: disable=no-value-for-parameter,unused-variable
"""Rotas de Financeiro"""
from flask import Blueprint

# from .rest import BotConversaView
# from .querys import BotQuerys

admin_app = Blueprint(
    "admin_app", __name__, url_prefix="/")

@admin_app.route('/')
def hello():
    return 'Hello World Tradicional de Cria!'