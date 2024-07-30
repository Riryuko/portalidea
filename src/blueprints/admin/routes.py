# pylint: disable=no-value-for-parameter,unused-variable
"""Rotas de Financeiro"""
from flask import Blueprint, request

# from .rest import BotConversaView
# from .querys import BotQuerys

admin_app = Blueprint(
    "admin_app", __name__, url_prefix="/alunos")

@admin_app.route('/criar', methods=['POST'])
def criar():
    """Rota para criar novo aluno"""

    dados = request.get_json()
    return 'Hello World Tradicional de Cria!'