from fastapi import FastAPI
import json 
import checks
import config



app = FastAPI(docs_url="/doc")

initMessage = "AEGIS API online"

@app.get("/")
async def root():
    return {initMessage}

@app.get("/health/services")
async def health():
    results = checks.check_services(config.url_list)
    return results

@app.get("/services")
async def health():
    return config.url_list

@app.get("/health/services")
async def health():
    results = checks.check_services(config.url_list)
    return results