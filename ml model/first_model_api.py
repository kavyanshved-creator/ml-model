"""# neaded things  = fastapi , uvicorn <- server 8000
# ,  basemodel <-body , @ <- abstraction
# , "/" <- routes

from first_model import model
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
 
app = FastAPI()

joblib.load("firstmodel.pkl")

class datascience(BaseModel):
    StudyHours:float 
    

# next step is to make the end poiunt 

@app.get("/")
def testing():
    return {"msg":"server is running"}


@app.post("/predict")
def datainsert(ds:datascience):

    marks = model.predict([[ds.StudyHours]])

    return ("predictmarks" : round(float(marks[0])))"""
# ---------------------------------------------------------------------

from fastapi.dependencies import models
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import joblib


app = FastAPI()

model_path = Path(__file__).parent / "firstmodel.pkl"
model = joblib.load(model_path)

class datascience(BaseModel):
    studyHours: float


# api end point

@app.get("/")
def test():
    return {"message": "uvicorn is running"}


@app.post("/predict")
def datainsert(ds:datascience):
    marks = model.predict([[ds.studyHours]])
    return{"predictionmarks":round(float(marks[0]),2)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("first_model_api:app", host="127.0.0.1", port=8000, reload=True)

