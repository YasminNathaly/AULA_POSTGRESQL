#db.py
#  pip instal psycopg2
# pip install dotenv (INSTALAÇAO DE UMA VERSÃO ESPECÍFICA)
import psycopg2
# PARA IMPORTAR DOTENV
from dotenv import load_dotenv
import os
load_dotenv()  # carrega as variaveis do .env
# PARA IMPORTAR arquivos de forma facilitada (import os)
# carrega as variaveis do .env
# conexão com o banco de dados
params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),

}
# PARAMETROS DE CONEXÃO
def connect():
    try:
        conexao = psycopg2.connect(**params)
        cursor = conexao.cursor()
        print('Deu certo')
        return conexao, cursor
    except Exception as erro:
        print("Erro ao conectar ao banco de dados:", {erro})
        # except é usado para tratar erros, evitar que o programa pare de funcionar
        return None, None
    
connect()