from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(request: CalculationRequest):
    result = request.a + request.b
    return {"result": result}

@app.post("/subtract")
def subtract(request: CalculationRequest):
    result = request.a - request.b
    return {"result": result}

@app.post("/multiply")
def multiply(request: CalculationRequest):
    result = request.a * request.b
    return {"result": result}

@app.post("/divide")
def divide(request: CalculationRequest):
    if request.b == 0:
        return {"error": "Cannot divide by zero"}
    result = request.a / request.b
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
