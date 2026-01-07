from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from validation.data_validation import UserInput
import pickle
import pandas as pd
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message":"Using Machine Learning Model with Fast API"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

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
