from fastapi import APIRouter
from database.databaseHandler import fetch_all_newsletter_people, delete_newsletter_person

router = APIRouter()

# 1. READ ALL - Pobranie listy do tabelki
@router.get("/api/newsletter")
async def get_all_newsletter():
    return fetch_all_newsletter_people()

# 2. DELETE - Usunięcie subskrybenta
@router.delete("/api/newsletter/{person_id}")
async def remove_newsletter_email(person_id: int):
    delete_newsletter_person(person_id)
    return {"message": "Usunięto pomyślnie"}
