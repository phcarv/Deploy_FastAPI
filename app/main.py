import sys
import os
sys.path.append("/code/app/")

# 1. Library imports
from typing import Dict
import uvicorn
from fastapi import FastAPI
from IrisData import IrisNewData
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
rf=pickle.load(open("app/randomforest.pkl","rb"))

# # 3. Index route, opens automatically on http://0.0.0.0:80
@app.get('/')
def index() -> Dict:
         """
         Get function of the index page.
         Returns instructions to the predict endpoint.
         """
         return {'message': 'O metodo get nao tem nenhuma informacao =c, va para o endpoint /predict e use o metodo post para ter a sua predicao'}

@app.post('/predict')
def predict_iris(data:IrisNewData) -> Dict:
     """
     Runs the prediction of the data that came from the IrisNewData class
     and returns that prediction
      
     Parameters:
         data = takes the values from the IrisNewData class that came from the POST request
        
     """
     data = data.dict()
     predict_df = pd.DataFrame(data, index=[0])
     prediction = rf.predict(predict_df)
     prediction = str(prediction)
     prediction_str = prediction[2:-2]
     return { 'Prediction' :  prediction_str}