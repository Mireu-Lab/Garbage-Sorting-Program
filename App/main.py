from fastapi import FastAPI, File, UploadFile
from models import model_run_main
import uvicorn
import shutil

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_location = f"Data/{file.filename}"
    
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)    
    
    return {"info": file_location, "status" : model_run_main(file_location)}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=1111)