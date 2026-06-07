import sqlite3

DATABASE_URL = "database/database.db"

#LOGIN
def verify_login(login, password):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("SELECT user_id, user_role FROM tbl_users WHERE user_login = ? AND user_password = ?", (login, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {"user_id": user[0], "user_role": user[1]}
    return None

#NEWS
def fetch_all_news():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT news_id, news_title, news_description, news_photo, news_date FROM tbl_news ORDER BY news_date DESC")
    rows = cursor.fetchall()
    conn.close()
    
    news_list = []
    for row in rows:
        news_list.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "image_path": row[3],
            "date": row[4]
        })
    return news_list

def insert_news(title, description, date, image_path):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tbl_news (news_title, news_description, news_photo, news_date) VALUES (?, ?, ?, ?)",
        (title, description, image_path, date)
    )
    conn.commit()
    conn.close()

def update_news(news_id, title, description, date, image_path=None):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    if image_path:
        cursor.execute(
            "UPDATE tbl_news SET news_title = ?, news_description = ?, news_date = ?, news_photo = ? WHERE news_id = ?",
            (title, description, date, image_path, news_id)
        )
    else:
        cursor.execute(
            "UPDATE tbl_news SET news_title = ?, news_description = ?, news_date = ? WHERE news_id = ?",
            (title, description, date, news_id)
        )
    
    conn.commit()
    conn.close()

def get_news_photo_path(news_id):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT news_photo FROM tbl_news WHERE news_id = ?", (news_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return None

def delete_news(news_id):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tbl_news WHERE news_id = ?", (news_id,))
    conn.commit()
    conn.close()

#GAMES
def fetch_all_games():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT game_id, game_name, game_description, game_photo FROM tbl_games ORDER BY game_id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    games_list = []
    for row in rows:
        games_list.append({
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "image_path": row[3]
        })
    return games_list
def insert_game(name, description, image_path):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tbl_games (game_name, game_description, game_photo) VALUES (?, ?, ?)",
        (name, description, image_path)
    )
    conn.commit()
    conn.close()
def update_game(game_id, name, description, image_path=None):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    if image_path:
        cursor.execute(
            "UPDATE tbl_games SET game_name = ?, game_description = ?, game_photo = ? WHERE game_id = ?",
            (name, description, image_path, game_id)
        )
    else:
        cursor.execute(
            "UPDATE tbl_games SET game_name = ?, game_description = ? WHERE game_id = ?",
            (name, description, game_id)
        )
    
    conn.commit()
    conn.close()
def get_game_photo_path(game_id):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT game_photo FROM tbl_games WHERE game_id = ?", (game_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return None
def delete_game(game_id):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tbl_games WHERE game_id = ?", (game_id,))
    conn.commit()
    conn.close()

#Newsletter
def fetch_all_newsletter_people():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT person_id, person_email FROM tbl_newsletters_people ORDER BY person_id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    people_list = []
    for row in rows:
        people_list.append({
            "id": row[0],
            "email": row[1]
        })
    return people_list
def delete_newsletter_person(person_id):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tbl_newsletters_people WHERE person_id = ?", (person_id,))
    conn.commit()
    conn.close()

def insert_newsletter_person(email):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tbl_newsletters_people (person_email) VALUES (?)", (email,))
    conn.commit()
    conn.close()