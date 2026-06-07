import sqlite3

DATABASE_URL = "database/SQLite.db"

def verify_login(login, password):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("SELECT user_id, user_role FROM tbl_users WHERE user_login = ? AND user_password = ?", (login, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {"user_id": user[0], "user_role": user[1]}
    return None
