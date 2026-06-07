from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database.databaseInit import databaseInit
from endpoints import adminEndpoints, newsEndpoints, gamesEndpoints, newsletterEndpoints

app = FastAPI()
databaseInit()

#CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(adminEndpoints.router, prefix="/api/admin", tags=["admin"])
app.include_router(newsEndpoints.router, tags=["news"])
app.include_router(gamesEndpoints.router, tags=["games"])
app.include_router(newsletterEndpoints.router, tags=["newsletter"])