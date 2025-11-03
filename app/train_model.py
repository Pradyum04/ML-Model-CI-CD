# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

data = load_iris()
X, y = data.data, data.target
model = RandomForestClassifier().fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
print("Model saved!")


#venv\Scripts\activate