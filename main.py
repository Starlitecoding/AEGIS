from fastapi import FastAPI
import json 

app = FastAPI()

initMessage = "AEGIS API online"

@app.get("/")
async def root():
    return json.dump(initMessage)


