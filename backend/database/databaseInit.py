import sqlite3
import os

def databaseInit():
    schemaPath = "database/schema.sql"
    dbName = "database/database.db"

    if os.path.exists(dbName):
        print("Baza danych juz istnieje.")
        return

    if not os.path.exists(schemaPath):
        print("Brak pliku schema.sql")
        return
    
    with open(schemaPath, "r", encoding="utf-8") as file:
        sqlScript = file.read()

    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    try:
        cursor.executescript(sqlScript)
        conn.commit()
        print("Baza danych pomyślnie zainicalizowana.")
    except sqlite3.Error as e:
        print(f"Błąd bazy danych: {e}")
    finally:
        conn.close()


