# Flask MySQL Application with Kubernetes

This project is a simple Flask application that retrieves random advice from a MySQL database. The application and the MySQL database are deployed using Kubernetes in separate containers.

## Prerequisites

Before starting, make sure you have the following tools installed:

1. **Docker**: You will use Docker to build images for the Flask app and MySQL database.
2. **Minikube**: A local Kubernetes cluster to test the application.
3. **Kubectl**: A command-line tool to interact with the Kubernetes cluster.
4. **Git**: To clone the repository.

## Project Structure

Here is the structure of the project:

```
├── flask-app/                   # Flask application
│   ├── Dockerfile               # Dockerfile to build the Flask app
│   ├── app.py                   # Main Flask application code
│   ├── requirements.txt         # Flask dependencies
│   ├── templates/               # HTML templates
│   │   ├── index.html
│   │   └── conseil.html
├── kubernetes/
│   ├── mysql-deployment.yaml    # MySQL Kubernetes deployment
│   ├── flask-deployment.yaml    # Flask Kubernetes deployment
│   ├── mysql-initdb-config.yaml # ConfigMap for MySQL initialization (init.sql)
└── README.md                    # This README file
```

## Installation and Setup

Follow these steps to set up the project and get it running in your local Kubernetes cluster using Minikube.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/flask-mysql-kubernetes.git
cd flask-mysql-kubernetes
```

### Step 2: Start Minikube

Make sure Minikube is installed and running.

```bash
minikube start
```

Configure Docker to use Minikube’s environment:

```bash
eval $(minikube -p minikube docker-env)
```

### Step 3: Build Docker Images

You need to build the Docker images for both the Flask application and the MySQL database.

#### Build the Flask application image

Navigate to the `flask-app/` directory and build the Docker image:

```bash
cd flask-app
docker build -t flask-app-image .
cd ..
```

#### Build the MySQL image (if necessary)

Since we are using the official MySQL image, there’s no need to build a custom MySQL image. However, you can modify the image version in the deployment file if needed.

### Step 4: Deploy MySQL and Flask to Kubernetes

#### Apply the ConfigMap for MySQL initialization

The ConfigMap contains the SQL script to create the database and populate the table with advice.

```bash
kubectl apply -f kubernetes/mysql-initdb-config.yaml
```

#### Deploy MySQL

Apply the MySQL deployment to Kubernetes:

```bash
kubectl apply -f kubernetes/mysql-deployment.yaml
```

Wait for the MySQL pod to be in the `Running` state:

```bash
kubectl get pods
```

#### Deploy Flask

Now, deploy the Flask application to Kubernetes:

```bash
kubectl apply -f kubernetes/flask-deployment.yaml
```

Check if the Flask pod is running:

```bash
kubectl get pods
```

### Step 5: Access the Application

Once both MySQL and Flask are deployed and running, you can access the Flask application through Minikube.

Expose the Flask service to access it from your browser:

```bash
minikube service flask-service --url
```

This will provide a URL (e.g., `http://192.168.99.100:5000`). Open this URL in your browser to access the application.

### Step 6: Test the Application

- The home page (`/`) should display a simple welcome page.
- The `/conseil` route will fetch a random advice from the MySQL database.

### Troubleshooting

If you encounter any issues, you can check the logs of the Flask and MySQL pods:

- **Check Flask logs**:

  ```bash
  kubectl logs <flask-pod-name>
  ```

- **Check MySQL logs**:

  ```bash
  kubectl logs <mysql-pod-name>
  ```

### Clean Up

To stop and remove all resources created by this project, run the following command:

```bash
kubectl delete -f kubernetes/mysql-deployment.yaml
kubectl delete -f kubernetes/flask-deployment.yaml
kubectl delete -f kubernetes/mysql-initdb-config.yaml
```

You can also stop Minikube:

```bash
minikube stop
```

## Project Details

### Technologies Used:

- **Flask**: Web framework used to create the application.
- **MySQL**: Database used to store advice.
- **Kubernetes**: Orchestrates the deployment of both Flask and MySQL in separate containers.
- **Docker**: Used to containerize the Flask application.

### Key Features:

- Flask application retrieves random advice from a MySQL database.
- Both Flask and MySQL run in separate Kubernetes pods.
- Automatic database initialization using an SQL script via Kubernetes ConfigMap.

---

Feel free to modify and adapt this README based on your project's specific needs!
