# Import Flask
from flask import Flask, request, jsonify

# Import du modèle sauvegardé
import joblib

# Import pandas
import pandas as pd

# Import CORS
from flask_cors import CORS

# -----------------------
# Création de l'application Flask
# -----------------------

app = Flask(__name__)

# Autorise les requêtes venant du frontend
CORS(app)

# -----------------------
# Chargement du modèle
# -----------------------

model = joblib.load("model.joblib")

# -----------------------
# Route de test
# -----------------------

@app.route("/")
def home():
    return "API en ligne !"

# -----------------------
# Route de prédiction
# -----------------------

@app.route("/predict", methods=["POST"])
def predict():
    # Récupère les données JSON envoyées
    data = request.json

    # Exemple :
    # { "surface": 50 }

    surface = data["surface"]

    # Convertit en DataFrame
    input_data = pd.DataFrame({
        "surface": [surface]
    })

    # Prédiction
    prediction = model.predict(input_data)

    # Retourne le résultat
    return jsonify({
        "prediction": round(prediction[0], 2)
    })

# -----------------------
# Lancement du serveur
# -----------------------

if __name__ == "__main__":
    app.run(debug=True)