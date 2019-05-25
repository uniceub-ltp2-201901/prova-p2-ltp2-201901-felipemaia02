from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import random
from db import *

#Felipe Oliveira Maia
#21801679

app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# configuracao do bd
config(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar')
def listar():
    # Obtendo o cursor para acessar o BD
    conn = mysql.connect()
    cursor = conn.cursor()

    links = get_links(cursor)

    # Fechar o cursor
    cursor.close()
    # Fechar a conexao
    conn.close()

    return render_template('links.html', links=links)

@app.route('/inserir', methods=['post'])
def inserir():
    if request.method == 'POST':
        # recuperar os parametros
        link_p = request.form.get('link_p')
        link_s = random.randint(00000, 99999)

        # Obtendo o cursor para acessar o BD
        conn = mysql.connect()
        cursor = conn.cursor()

        # inserindo o contato
        set_user(cursor, conn, link_p, link_s)

        # Fechar o cursor
        cursor.close()
        # Fechar a conexao
        conn.close()

        # retornando a lista de contatos
        return redirect(url_for('listar'))

    else:
        index()



if __name__ == '__main__':
    app.run(debug=True)