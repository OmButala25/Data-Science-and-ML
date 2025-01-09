
#import libraries
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pickle
import pandas as pd
import numpy as np

#create an app
app = FastAPI()
pickle_in = open("model.pkl", "rb")
classifier = pickle.load(pickle_in)

#Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message':'Welcome to the BankNote Prediction'}

#Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def welcome_again(name: str):
    return {'Welcome to the another page': f'{name}'}

#Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data: BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])

    if(prediction[0]>0.5):
        prediction= 'Fake Note'
    else:
        prediction= "It's a Bank Note"
    return {
        'prediction' : prediction
    }

#Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

#uvicorn app:app --reload
# or try -> python -m uvicorn app:app --reload