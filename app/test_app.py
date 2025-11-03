import json
from app import app

def test_predict():
    tester = app.test_client()
    response = tester.post("/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]}
    )
    assert response.status_code == 200
