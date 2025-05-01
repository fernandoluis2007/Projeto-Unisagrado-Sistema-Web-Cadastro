from main import app # Importa o app do arquivo main, para poder rodar normalmente o programa
from flask import render_template # importar do Flask, a renderização de um template!
from flask import request

# Rota Home Page -->

@app.route('/') # Rota para Home Page! (Route) == Rota!
def homepage(): # Função para carregar as informações que vão apararecer nesta rota!
    return render_template('homepage.html')   

# <-- Fim da Rota Home Page 

@app.route('/blog')
def blogpage():
    return 'Blog!'

@app.route('/formulario', methods=['GET', 'POST'])
def formulariopage():
    if request.method == 'POST':
        nome = request.form['nomeForm']
        email= request.form['emailForm']
        print(f'{nome} | {email}')
    return render_template('formulario.html')