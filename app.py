from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from utils import generate_art_code, modify_art_code
import uvicorn

app = FastAPI()
security = HTTPBearer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateCodeRequest(BaseModel):
    userPrompt: str

class RunCodeRequest(BaseModel):
    code: str

class ModifyArtCodeRequest(BaseModel):
    code: str
    userPrompt: str

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return credentials.credentials

@app.post("/generate_code")
async def generate_code(
    request: GenerateCodeRequest,
    token: str = Depends(verify_token)
):
    generated_code = generate_art_code(request.userPrompt)
    return {"code": generated_code}

@app.post("/modify_art_code")
async def modify_art_code(
    request: ModifyArtCodeRequest,
    token: str = Depends(verify_token)
):
    modified_code = modify_art_code(request.code, request.userPrompt)
    return {"code": modified_code}

@app.post("/run_code")
async def run_code(
    request: RunCodeRequest,
    token: str = Depends(verify_token)
):
    exec(request.code)
    return {"output": "output.png"}
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
