from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import FileResponse
from pydantic import BaseModel
from utils import generate_art_code, modify_art_code
import uvicorn
import os
import tempfile
import subprocess

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
    try:
        # Write the code to a file
        code_file_path = "generated_art_script.py"
        with open(code_file_path, 'w') as file:
            file.write(request.code)
        
        # Run the code in a separate process
        result = subprocess.run(['python', code_file_path], 
                              capture_output=True, 
                              text=True, 
                              timeout=30)  # 30 second timeout
        
        # Clean up the file
        os.remove(code_file_path)
        
        if result.returncode != 0:
            raise Exception(f"Code execution failed:\n{result.stderr}")
            
        print("Code executed successfully")
        
        # Check if the file exists
        output_path = "output.png"
        if not os.path.exists(output_path):
            raise HTTPException(status_code=404, detail="Image was not generated")
            
        # Return the actual image file
        return FileResponse(
            output_path,
            media_type="image/png",
            filename="generated_art.png"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
