from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from validation.data_validation import UserInput
import pickle
import pandas as pd

app = FastAPI()

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message":"Using Machine Learning Model with Fast API"}

@app.post("/predict")
def predict_premium(data: UserInput):

    try:
        input_data = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
        }])

        prediction = model.predict(input_data)[0]

        if prediction:
            return JSONResponse(status_code=200, content={"prediction":prediction})
    except Exception:
        raise HTTPException(status_code=400, detail={"error":"failed to respond"})
