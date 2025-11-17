from flask import Flask, render_template, abort

app = Flask(__name__)

carros_lancamentos = [
    {"nome": "Corolla", "desc": "2.0 Flex CVT", "preco": "R$ 149.990,00"},
    {"nome": "Civic", "desc": "2.0 Turbo", "preco": "R$ 189.990,00"},
    {"nome": "Pulse", "desc": "SUV Turbo 200", "preco": "R$ 108.490,00"},
]

carros_bmw = [
    {"nome": "Z4", "desc": "Roadster 2.0 Turbo", "preco": "R$ 399.900,00"},
    {"nome": "X1", "desc": "SUV xDrive 2.0", "preco": "R$ 279.900,00"},
    {"nome": "M5", "desc": "4.4 V8 Turbo", "preco": "R$ 1.199.900,00"},
]

@app.route('/carro/<nome>')
def carro_detalhes(nome):
    # Procura o carro pelo nome nas duas listas
    carro = next((c for c in carros_lancamentos if c['nome'].lower() == nome.lower()), None)
    if not carro:
        carro = next((c for c in carros_bmw if c['nome'].lower() == nome.lower()), None)
    if not carro:
        # Retorna erro 404 se não encontrar o carro
        abort(404)
    
    # Passa o carro encontrado e uma imagem fictícia (ajuste conforme seu sistema)
    car_img = f"/static/images/{carro['nome'].lower()}.jpg" 

    return render_template('seu_template.html', c=carro, car={'img': car_img, 'name': carro['nome']})

