# Utiliser une image officielle de MySQL
FROM mysql:5.7

# Copier le fichier SQL d'initialisation dans le répertoire d'entrée de MySQL
COPY init.sql /docker-entrypoint-initdb.d/

# Configuration des variables d'environnement
ENV MYSQL_DATABASE=advices
ENV MYSQL_ROOT_PASSWORD=example
