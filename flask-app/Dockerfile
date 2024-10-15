# Utilise une image Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "app.py"]
