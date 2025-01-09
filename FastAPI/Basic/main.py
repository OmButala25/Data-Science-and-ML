
import uvicorn #ASGI
from fastapi import FastAPI

#create an app object you can use any name here I will use app
app = FastAPI()

#create bydefault Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {"Hello World"}

# Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/welcome')
def welcome(name : str):
    return {"Welcome to the Om's Webpage" : f'{name}'}


#  Run the API with uvicorn
#  Will run on http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn main:app --reload
# or try -> python -m uvicorn main:app --reload