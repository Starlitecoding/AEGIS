import uuid

from fastapi import FastAPI
from fastapi import HTTPException
import checks
import config
from models import ServiceCreate 


app = FastAPI(docs_url="/doc")

initMessage = "AEGIS API, v1.0"

list_services = []

@app.get("/")
async def root():
    return {"message": initMessage}


@app.get("/health/live")
async def api_health_live():
    return {"status": "api alive"}


@app.get("/health/ready")
async def api_health_ready():
    return {"status": "200"}

@app.get("/services")
async def service_list():
    return list_services

@app.get("/health/services")
def service_health():
    list_url = []
    for i in list_services:
        list_url.append(i["url"])
    

    results = checks.check_services(list_url)
    return results


@app.post("/service_add", status_code=201)
async def create_service(input: ServiceCreate):
    new_service = {
        "service_id": str(uuid.uuid4()),
        "name": input.name,
        "url": str(input.url)
    }
    

    for i in list_services:
        if i["url"] == str(input.url):
            raise HTTPException(status_code=409, detail="Service with this URL already exists")
        
            
    list_services.append(new_service)        
    return new_service


@app.delete("/service_delete/{item_id}")
async def delete_service(item_id: str):
    for i in list_services:
        if item_id == i["service_id"]:
            list_services.remove(i)
            return {"message": f"Service {i['name']} removed"}
    raise HTTPException(status_code=404, detail="Service not found")

                 
            
            
            
            
    
