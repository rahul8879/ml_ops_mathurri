## you will create API --> input from user -->return the status
from fastapi import FastAPI
import pickle

app = FastAPI()
model = pickle.load(open('model.pkl', 'rb'))


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/predict")
def predict(cibile_score, income):
    print( 'type of input ',type(cibile_score), type(income))
    input = [int(cibile_score), int(income)] #[cibile_score, income]
    
    output = model.predict([input])

    return {
        "status": output[0]
    }
    




@app.get("/predict/{age}")
async def predict(age):
    return model.predict([[age]])