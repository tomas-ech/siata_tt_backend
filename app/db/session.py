from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config.settings import env_settings

engine = create_engine(env_settings.DATABASE_URL)

db = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = db()
    try:
        yield session
    finally:
        session.close()