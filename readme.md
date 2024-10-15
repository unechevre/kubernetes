
```md
# Application Flask avec MySQL et Kubernetes

Ce projet est une application Flask simple qui récupère des conseils aléatoires depuis une base de données MySQL. L'application et la base de données MySQL sont déployées sur Kubernetes dans des conteneurs séparés.

## Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés :

1. **Docker**
2. **Minikube**
3. **Kubectl**
4. **Git**

## Installation

<details>
  <summary><strong>Installation sous Linux</strong></summary>

### Étape 1 : Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/flask-mysql-kubernetes.git
cd flask-mysql-kubernetes
```

### Étape 2 : Démarrer Minikube

```bash
minikube start
```

### Étape 3 : Configurer Docker pour Minikube

```bash
eval $(minikube -p minikube docker-env)
```

### Étape 4 : Construire et déployer les images

#### Construire l'image Flask :

```bash
cd flask-app
docker build -t flask-app-image .
cd ..
```

#### Appliquer le ConfigMap et les déploiements MySQL et Flask

```bash
kubectl apply -f kubernetes/mysql-initdb-config.yaml
kubectl apply -f kubernetes/mysql-deployment.yaml
kubectl apply -f kubernetes/flask-deployment.yaml
```

### Étape 5 : Accéder à l'application

Exposez le service Flask :

```bash
minikube service flask-service --url
```

Cela fournira une URL comme `http://192.168.99.100:5000`. Ouvrez cette URL dans votre navigateur pour accéder à l'application.

</details>

<details>
  <summary><strong>Installation sous Windows</strong></summary>

### Étape 1 : Cloner le dépôt

Ouvrez **PowerShell** et exécutez :

```bash
git clone https://github.com/votre-utilisateur/flask-mysql-kubernetes.git
cd flask-mysql-kubernetes
```

### Étape 2 : Démarrer Minikube

```bash
minikube start
```

### Étape 3 : Configurer Docker pour Minikube

Dans **PowerShell**, configurez Docker pour utiliser l'environnement de Minikube :

```bash
minikube docker-env | Invoke-Expression
```

### Étape 4 : Construire et déployer les images

#### Construire l'image Flask :

```bash
cd flask-app
docker build -t flask-app-image .
cd ..
```

#### Appliquer le ConfigMap et les déploiements MySQL et Flask

```bash
kubectl apply -f kubernetes/mysql-initdb-config.yaml
kubectl apply -f kubernetes/mysql-deployment.yaml
kubectl apply -f kubernetes/flask-deployment.yaml
```

### Étape 5 : Accéder à l'application

Exposez le service Flask :

```bash
minikube service flask-service --url
```

Cela fournira une URL comme `http://192.168.99.100:5000`. Ouvrez cette URL dans votre navigateur pour accéder à l'application.

</details>

---

## Nettoyage

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

## Détails du projet

### Technologies utilisées :

- **Flask** : Framework web utilisé pour créer l'application.
- **MySQL** : Base de données pour stocker les conseils.
- **Kubernetes** : Orchestration du déploiement de Flask et MySQL dans des conteneurs séparés.
- **Docker** : Utilisé pour containeriser l'application Flask.

### Fonctionnalités principales :

- L'application Flask récupère des conseils aléatoires depuis une base de données MySQL.
- Flask et MySQL s'exécutent dans des pods Kubernetes séparés.
- Initialisation automatique de la base de données avec un script SQL via ConfigMap.

---

## Dépannage

Si vous rencontrez des problèmes, vous pouvez vérifier les journaux des pods Flask et MySQL :

- **Voir les logs de Flask** :

  ```bash
  kubectl logs <nom-du-pod-flask>
  ```

- **Voir les logs de MySQL** :

  ```bash
  kubectl logs <nom-du-pod-mysql>
  ```
