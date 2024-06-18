from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def calcular_horas_disponiveis(data_inicial_str, intervalos_usados=None):
    try:
        data_inicial = datetime.strptime(data_inicial_str, '%d-%m-%Y')
    except ValueError:
        return 'Formato de data inválido para data inicial', False

    data_atual = datetime.now()

    if data_inicial > data_atual:
        return 'Data inicial não pode ser no futuro', False

    diferenca_dias = (data_atual - data_inicial).days + 1
    horas_disponiveis = diferenca_dias * 10

    if intervalos_usados:
        for intervalo in intervalos_usados:
            try:
                data_inicio = datetime.strptime(intervalo['data_inicio'], '%d-%m-%Y')
                data_fim = datetime.strptime(intervalo['data_fim'], '%d-%m-%Y')
            except ValueError:
                return 'Formato de data inválido para um dos intervalos', False

            if data_inicio > data_fim:
                return 'Data de início do intervalo não pode ser posterior à data de fim', False

            diferenca_intervalo = (data_fim - data_inicio).days + 1
            horas_disponiveis -= diferenca_intervalo * 10

    return horas_disponiveis, True

@app.route('/')
def home():
    data_inicial_usuario = '01-01-2023'
    intervalos_usados = [{'data_inicio': '03-06-2024', 'data_fim': '06-06-2024'}]
    total_horas, sucesso = calcular_horas_disponiveis(data_inicial_usuario, intervalos_usados)
    if sucesso:
        return f"Total de horas disponíveis do usuário desde {data_inicial_usuario} considerando intervalos usados: {total_horas} horas"
    else:
        return total_horas, 400

@app.route('/horas_disponiveis', methods=['POST'])
def get_horas_disponiveis():
    data = request.json
    data_inicial = data.get('data_inicial')
    intervalos_usados = data.get('intervalos_usados')

    if data_inicial:
        horas, sucesso = calcular_horas_disponiveis(data_inicial, intervalos_usados)
        if sucesso:
            return jsonify({'horas_disponiveis': horas}), 200
        else:
            return jsonify({'error': horas}), 400
    else:
        return jsonify({'error': 'Data inicial não fornecida'}), 400

if __name__ == '__main__':
    app.run(debug=True)
