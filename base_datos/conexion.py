from sqlalchemy import create_engine

def conectar():
    conexion = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/sistema_escolar")


    return conexion
