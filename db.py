from flaskext.mysql import MySQL

# função para configurar o acesso a banco
def config(app):
    # Configurando o acesso ao MySQL
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'prova2'

# Retorna conexao e cursor
def get_db(mysql):
    # Obtendo o cursor para acessar o BD
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

def get_links(cursor):
    # Executar o SQL
    cursor.execute('SELECT link_p, link_s FROM prova2.link')

    # Recuperando o retorno do BD
    links = cursor.fetchall()

    # Retornar os dados
    return links


def set_user(cursor, conn, link_p, link_s):
    cursor.execute(f'insert into  prova2.link (link_p, link_s) values("{link_p}", "{link_s}")')
    conn.commit()