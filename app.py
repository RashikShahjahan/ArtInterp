import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import generate_art_code, modify_art_code
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request models
class GenerateCodeRequest(BaseModel):
    userPrompt: str

class RunCodeRequest(BaseModel):
    code: str

class ModifyArtCodeRequest(BaseModel):
    code: str
    userPrompt: str

@app.post("/generate_code")
async def generate_code(request: GenerateCodeRequest):
    try:
        generated_code = generate_art_code(request.userPrompt)
        return {"code": generated_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/modify_art_code")
async def modify_art_code(request: ModifyArtCodeRequest):
    try:
        modified_code = modify_art_code(request.code, request.userPrompt)
        return {"code": modified_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run_code")
async def run_code(request: RunCodeRequest):
    try:
        exec(request.code)
        return {"result": "Code executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
