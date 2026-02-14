from app.db.session import engine
from app.models import Base

def reset_database():
    print("ALERTA: Se eliminarán todos los datos existentes.")
    confirm = input("¿Estás seguro de que quieres continuar? (s/n): ")
    
    if confirm.lower() == 's':
        try:
            print("Eliminando tablas existentes...")
            Base.metadata.drop_all(bind=engine)
            
            print("Creando tablas...")
            Base.metadata.create_all(bind=engine)
            
            print("-- Base de datos sincronizada con éxito --")
        except Exception as e:
            print("ERROR: " + e)
    else:
        print("Cancelado el proceso")

if __name__ == "__main__":
    reset_database()