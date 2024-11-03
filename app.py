from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import generate_art_code, modify_art_code
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    generated_code = generate_art_code(request.userPrompt)
    return {"code": generated_code}
 
@app.post("/modify_art_code")
async def modify_art_code(request: ModifyArtCodeRequest):
    modified_code = modify_art_code(request.code, request.userPrompt)
    return {"code": modified_code}

@app.post("/run_code")
async def run_code(request: RunCodeRequest):
    exec(request.code)
    return {"output": "output.png"}
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
