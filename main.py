from flask import Flask # importar o Flask!


app = Flask(__name__) # Criar o App!

# Rotas do site -->

from views import * # importa todas(*) as rotas do arquivo views.py

# <-- Fim das Rotas

if __name__ == '__main__':
    app.run() # Rodando o programa.