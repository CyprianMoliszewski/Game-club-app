from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
import os

from helpers.file_utils import save_upload_file
from database.databaseHandler import (
    fetch_all_news, 
    insert_news, 
    update_news, 
    delete_news, 
    get_news_photo_path
)

router = APIRouter()
UPLOAD_DIR = "assets/news"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/api/news")
async def get_all_news():
    return fetch_all_news()

@router.post("/api/news")
async def create_news(
    title: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    image: UploadFile = File(...) 
):
    file_location = await save_upload_file(image, UPLOAD_DIR)

    insert_news(title, description, date, file_location)
    return {"message": "Dodano wpis pomyślnie"}

@router.put("/api/news/{news_id}")
async def edit_news(
    news_id: int,
    title: str = Form(..., min_length=1, max_length=100),
    description: str = Form(..., min_length=1),
    date: str = Form(..., pattern=r"^\d{2}-\d{2}-\d{4}$"),
    image: Optional[UploadFile] = File(None) 
):
    file_location = None

    if image is not None and image.filename != "":

        file_location = await save_upload_file(image, UPLOAD_DIR)

        old_photo = get_news_photo_path(news_id)
        if old_photo and os.path.exists(old_photo):
            os.remove(old_photo)
            
    update_news(news_id, title, description, date, image_path=file_location)
    
    return {"message": "Zaktualizowano wpis pomyślnie"}

@router.delete("/api/news/{news_id}")
async def remove_news(news_id: int):
    photo_path = get_news_photo_path(news_id)

    if photo_path and os.path.exists(photo_path):
        os.remove(photo_path)

    delete_news(news_id)
    
    return {"message": "Usunięto pomyślnie"}
