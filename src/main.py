import uvicorn
import os
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

'''
Event Types
'''


class Payload(BaseModel):
    class Config:
        extra = "allow"


class Body(BaseModel):
    eventId: str
    validTime: str
    payload: Payload


'''
Required Health Check
'''


@app.get("/health")
def health():
    return {}


'''
Transformer
'''


@app.post("/transform")
async def transform(body: Body):
    result = {}
    for key, value in body.payload.dict().items():
        # Check if the value is a string
        if not isinstance(value, str):
            # Convert non-strings to JSON format using json.dumps()
            value = json.dumps(value, separators=(",",":"))
        # Add the key-value pair to the result object
        result[key] = value

    return {"eventId": body.eventId, "validTime": body.validTime, **result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ["PORT"]), log_level="info")
