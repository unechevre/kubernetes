## Application Flask avec MySQL et Kubernetes

Ce projet est une simple application Flask qui récupère des conseils aléatoires à partir d'une base de données MySQL. L'application et la base de données MySQL sont déployées à l'aide de Kubernetes dans des conteneurs séparés.

### Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés :

- **Docker** : Pour construire les images de l'application Flask et de la base de données MySQL.
- **Minikube** : Un cluster Kubernetes local pour tester l'application.
- **Kubectl** : Un outil en ligne de commande pour interagir avec le cluster Kubernetes.
- **Git** : Pour cloner le dépôt du projet.

### Structure du Projet

Voici la structure du projet :

```bash
Copier le code
├── flask-app/                   # Application Flask
│   ├── Dockerfile               # Dockerfile pour construire l'application Flask
│   ├── app.py                   # Code principal de l'application Flask
│   ├── requirements.txt         # Dépendances Flask
│   ├── templates/               # Templates HTML
│   │   ├── index.html
│   │   └── conseil.html
├── kubernetes/
│   ├── mysql-deployment.yaml    # Déploiement Kubernetes pour MySQL
│   ├── flask-deployment.yaml    # Déploiement Kubernetes pour Flask
│   ├── mysql-initdb-config.yaml # ConfigMap pour l'initialisation de MySQL (init.sql)
└── README.md                    # Ce fichier README
```

### Installation et Configuration

Suivez ces étapes pour configurer le projet et l'exécuter dans votre cluster Kubernetes local avec Minikube.

#### Étape 1 : Cloner le dépôt

```bash
git clone https://github.com/your-username/flask-mysql-kubernetes.git
cd flask-mysql-kubernetes
```

#### Étape 2 : Démarrer Minikube

Assurez-vous que Minikube est installé et en cours d'exécution.

```bash
minikube start
```

Configurez Docker pour utiliser l'environnement de Minikube :

```bash
minikube docker-env | Invoke-Expression
```

#### Étape 3 : Construire les images Docker

Vous devez construire les images Docker pour l'application Flask et la base de données MySQL.

Construire l'image de l'application Flask
Allez dans le répertoire flask-app/ et construisez l'image Docker :

```bash
cd flask-app
docker build -t flask-app-image .
cd ..
```

Construire l'image MySQL (si nécessaire)
Comme nous utilisons l'image officielle de MySQL, il n'est pas nécessaire de construire une image MySQL personnalisée. Cependant, vous pouvez modifier la version de l'image dans le fichier de déploiement si nécessaire.

#### Étape 4 : Déployer MySQL et Flask sur Kubernetes

Appliquez tous les fichiers YAML à Kubernetes avec la commande suivante :

```bash
kubectl apply -f kubernetes/
```

Vérifiez si les pods sont en cours d'exécution :

```bash
kubectl get pods
```

#### Étape 5 : Accéder à l'Application

Une fois MySQL et Flask déployés et en cours d'exécution, vous pouvez accéder à l'application Flask via Minikube.

Exposez le service Flask pour y accéder depuis votre navigateur :

```bash
minikube service flask-service --url
```

Cela fournira une URL (par exemple, http://127.0.0.1:5000). Ouvrez cette URL dans votre navigateur pour accéder à l'application.

#### Étape 6 : Tester l'Application

La page d'accueil (/) doit afficher une simple page d'accueil.
La route /conseil récupère un conseil aléatoire depuis la base de données MySQL.
Dépannage
Si vous rencontrez des problèmes, vous pouvez consulter les journaux des pods Flask et MySQL :

Consulter les journaux de Flask :

```bash
kubectl logs <flask-pod-name>
```

Consulter les journaux de MySQL :

```bash
kubectl logs <mysql-pod-name>
```

#### Nettoyage

Pour arrêter et supprimer toutes les ressources créées par ce projet, exécutez les commandes suivantes :

```bash
kubectl delete -f kubernetes/mysql-deployment.yaml
kubectl delete -f kubernetes/flask-deployment.yaml
kubectl delete -f kubernetes/mysql-initdb-config.yaml
```

Vous pouvez également arrêter Minikube :

```bash
minikube stop
```

### Détails du Projet

Technologies Utilisées :

- **Flask** : Framework web utilisé pour créer l'application.
- **MySQL** : Base de données pour stocker les conseils.
- **Kubernetes** : Orchestration du déploiement de Flask et MySQL dans des conteneurs séparés.
- **Docker** : Utilisé pour containeriser l'application Flask.

#### Fonctionnalités Clés :

L'application Flask récupère des conseils aléatoires depuis une base de données MySQL.
Flask et MySQL fonctionnent dans des pods Kubernetes séparés.
Initialisation automatique de la base de données via un script SQL grâce à ConfigMap de Kubernetes.