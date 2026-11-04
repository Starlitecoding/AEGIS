from fastapi import FastAPI
import checks
import config
from models import ServiceCreate 


app = FastAPI(docs_url="/doc")

initMessage = "AEGIS API, v1.0"

@app.get("/")
async def root():
    return {"message": initMessage}

# The localhost will be changed to real ip later, need to add flexible var instead of ip
@app.get("/health/live")
async def api_health_live():
    return {"status": "api alive"}

# The localhost will be changed to real ip later, need to add flexible var instead of ip
@app.get("/health/ready")
async def api_health_ready():
    return {"status": "200"}

@app.get("/services_list")
async def service_list():
    return config.url_list

@app.get("/health/services")
def service_health():
    results = checks.check_services(config.url_list)
    return results

@app.post("/services")
async def create_service(input: ServiceCreate):
    return input
