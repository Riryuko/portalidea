from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def calcular_horas_disponiveis(data_inicial_str):
    data_inicial = datetime.strptime(data_inicial_str, '%d.%m.%Y')
    data_atual = datetime.now()
    diferenca_dias = (data_atual - data_inicial).days + 1 
    horas_disponiveis = diferenca_dias * 10
    return horas_disponiveis

@app.route('/')
def home():
    data_inicial_usuario = '01.01.2023' 
    total_horas = calcular_horas_disponiveis(data_inicial_usuario)
    return f"Total de horas disponíveis do usuário desde {data_inicial_usuario}: {total_horas} horas"

@app.route('/horas_disponiveis', methods=['POST'])
def get_horas_disponiveis():
    data_inicial = request.json.get('data_inicial')
    if data_inicial:
        horas = calcular_horas_disponiveis(data_inicial)
        return jsonify({'horas_disponiveis': horas}), 200
    else:
        return jsonify({'error': 'Data inicial não fornecida'}), 400