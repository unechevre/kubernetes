import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import time
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

# Récupère l'URI de la base de données depuis les variables d'environnement
database_uri = os.getenv('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:example@mysql-service:3306/advices')
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle de données pour la table des conseils
class Advice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

@app.before_first_request
def create_tables():
    retries = 5
    while retries > 0:
        try:
            db.create_all()  # Create database tables if they do not exist
            break
        except OperationalError:
            retries -= 1
            time.sleep(5)  # Wait before retrying
            print("Retrying database connection...")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/conseil")
def conseil():
    try:
        advice = Advice.query.order_by(db.func.random()).first()
        return render_template("conseil.html", conseil=advice.text)
    except Exception as e:
        print(f"Erreur : {e}")
        return render_template("error.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)