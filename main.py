from fastapi import FastAPI
from typing import Union, Any
import uvicorn
import json
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from transformers import pipeline

app = FastAPI()

origins = ["http://localhost","http://localhost:3000",]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FoodTruck(BaseModel):
    locationid: str
    Applicant: str
    FacilityType: str
    cnn: str
    LocationDescription: str
    Address: str
    blocklot: str
    block: str
    lot: str
    permit: str
    Status: str
    FoodItems: str
    X: str
    Y: str
    Latitude: str
    Longitude: str
    Schedule: str
    dayshours: str
    NOISent: str
    Approved: str
    Received: str
    PriorPermit: str
    ExpirationDate: str
    Location: str
    FirePreventionDistricts: str
    PoliceDistricts: str
    SupervisorDistricts: str
    ZipCodes: str
    Neighborhoods: str

with open("data.json", 'r') as f:
    temp = json.loads(f.read())
    print(temp)

@app.get("/")
def read_root():
    return{"Hello": "World"}

@app.get("/foodtrucks/", response_model=list[FoodTruck])
async def read_items() -> Any:
    return temp

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)