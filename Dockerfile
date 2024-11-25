# Utiliser l'image officielle de Python comme base
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier pyproject.toml
COPY pyproject.toml ./

# Installer les dépendances spécifiées dans pyproject.toml
RUN pip install --upgrade pip setuptools wheel && \
    pip install .

# Copier le code de l'application
COPY ./app ./app

# Définir le répertoire de travail pour l'application
WORKDIR /app/app

# Exposer le port sur lequel l'application s'exécute
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
