from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration de la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@mysql-service:3306/advices'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle de données pour la table des conseils
class Advice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

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
