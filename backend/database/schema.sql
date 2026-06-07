CREATE TABLE tbl_news (
    news_id INTEGER PRIMARY KEY AUTOINCREMENT,
    news_title TEXT NOT NULL,
    news_description TEXT NOT NULL,
    news_photo TEXT NOT NULL,
    news_date DATETIME NOT NULL
);

CREATE TABLE tbl_games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name TEXT NOT NULL,
    game_photo TEXT NOT NULL,
    game_description TEXT not NULL
);

CREATE TABLE tbl_users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_login TEXT NOT NULL UNIQUE,
    user_password TEXT NOT NULL,
    user_role TEXT not NULL
);

CREATE TABLE tbl_newsletters_people (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_email TEXT NOT NULL UNIQUE
);