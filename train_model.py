import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# -----------------------
# 1. Création d'un dataset simple
# -----------------------

# Surface des maisons (en m²)
X = pd.DataFrame({
    'surface': [20, 30, 40, 50, 60, 70, 80]
})

# Prix des maisons 
y = [100000, 140000, 180000, 220000, 260000, 300000, 340000]

# -----------------------
# 2. Création d'un modèle 
# -----------------------

model = LinearRegression()

# -----------------------
# 3. Entraînement du modèle
# -----------------------

model.fit(X, y)

# -----------------------
# 4. Sauvegarde du modèle  
# -----------------------

joblib.dump(model, "model.joblib")

print("Modèle entrainé et sauvegardé")