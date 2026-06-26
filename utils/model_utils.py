import joblib

model = joblib.load("placement_model.pkl")


def predict(data):
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]

    return prediction, probability
