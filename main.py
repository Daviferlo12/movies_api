from fastapi import FastAPI


app = FastAPI()
app.title = "MOVIES API"
app.version = "0.0.1"

@app.get('/')
def message():
    return "Hola mundo ¿"