import os
import shutil
import uuid
from fastapi import UploadFile, HTTPException

MAX_FILE_SIZE = 5 * 1024 * 1024 # 5 MB

async def save_upload_file(upload_file: UploadFile, destination_folder: str) -> str:
    if upload_file.content_type != "image/png":
        raise HTTPException(status_code=400, detail="Akceptujemy wyłącznie format PNG.")
        
    if getattr(upload_file, "size", 0) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Plik jest za duży! (Maksymalnie 5MB)")
    
    os.makedirs(destination_folder, exist_ok=True)
    
    file_ext = upload_file.filename.split(".")[-1]
    new_filename = f"{uuid.uuid4()}.{file_ext}"
    file_location = os.path.join(destination_folder, new_filename)
    
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(upload_file.file, file_object)

    return file_location.replace('\\', '/')
