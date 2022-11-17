CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    is_admin BOOLEAN
);

CREATE TABLE meetings (
    id SERIAL PRIMARY KEY,
    meeting_name TEXT,
    meeting_date DATE,
    meeting_time TIME
);

CREATE TABLE Officers (
    user_id INTEGER,
    meeting_id INTEGER,
    meetingofficer BOOLEAN,
    votecounter BOOLEAN
);