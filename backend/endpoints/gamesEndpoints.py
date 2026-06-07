from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
import os


from helpers.file_utils import save_upload_file
from database.databaseHandler import (
    fetch_all_games,
    insert_game,
    update_game,
    delete_game,
    get_game_photo_path)

router = APIRouter()
UPLOAD_DIR = "assets/games"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 1. READ ALL
@router.get("/api/games")
async def get_all_games():
    return fetch_all_games()

# 2. CREATE 
@router.post("/api/games")
async def create_game(
    name: str = Form(..., min_length=1, max_length=100),
    description: str = Form(..., min_length=1),
    image: UploadFile = File(...) 
):
    file_location = await save_upload_file(image, UPLOAD_DIR)
        
    insert_game(name, description, file_location)
    return {"message": "Dodano grę pomyślnie"}

# 3. UPDATE 
@router.put("/api/games/{game_id}")
async def edit_game(
    game_id: int,
    name: str = Form(..., min_length=1, max_length=100),
    description: str = Form(..., min_length=1),
    image: Optional[UploadFile] = File(None) 
):
    file_location = None
    
    if image is not None and image.filename != "":

        file_location = await save_upload_file(image, UPLOAD_DIR)

        old_photo = get_game_photo_path(game_id)
        if old_photo and os.path.exists(old_photo):
            os.remove(old_photo)
            
    update_game(game_id, name, description, image_path=file_location)
    return {"message": "Zaktualizowano grę pomyślnie"}

# 4. DELETE 
@router.delete("/api/games/{game_id}")
async def remove_game(game_id: int):
    photo_path = get_game_photo_path(game_id)
    if photo_path and os.path.exists(photo_path):
        os.remove(photo_path)
        
    delete_game(game_id)
    return {"message": "Usunięto pomyślnie"}
