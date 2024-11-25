from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# URL de connexion à la base de données
DATABASE_URL = "sqlite:///./test.db"

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Configuration de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Fournit une session de base de données pour les dépendances FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
