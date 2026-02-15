from sqlalchemy import text
from app.db.session import engine

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Conexión exitosa")
            print(f"Resultado de la consulta: {result.fetchone()}")
    except Exception as e:
        print("Error al conectar")
        print(e)

if __name__ == "__main__":
    test_connection()