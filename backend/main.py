from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Waterjade Hydrology API")

# Configurazione CORS per permettere le richieste dal frontend Angular (solitamente http://localhost:4200)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Waterjade Hydrology API"}

# TODO: Aggiungere gli endpoint per leggere i dati idrologici e calcolare la media mobile
