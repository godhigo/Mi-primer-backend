#importamos las bibliotecas
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Mi primer intento"

@app.route('/saludos')
def saludos():
    return "Que onda"
    

if __name__ == '__main__':
    app.run(debug=True)
