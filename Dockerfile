# 1. Utiliser une image Python légère
FROM python:3.11-slim

# 2. Définir le répertoire de travail
WORKDIR /app

# 3. Copier le fichier requirements.txt
COPY requirements.txt .

# 4. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le reste du projet dans le conteneur
COPY . .

# 6. Exposer le port 5000
EXPOSE 5000

# 7. Démarrer le serveur Flask
CMD ["flask", "run", "--host=0.0.0.0"]
