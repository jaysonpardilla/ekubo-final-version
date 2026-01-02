import sqlite3
import shutil
import os

DB='db.sqlite3'
BACKUP='db.sqlite3.bak'
if os.path.exists(DB):
    print('Backing up', DB, '->', BACKUP)
    shutil.copy2(DB, BACKUP)
else:
    print('Database file not found:', DB)
    raise SystemExit(1)

con=sqlite3.connect(DB)
cur=con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='chat_profile';")
if cur.fetchone():
    print('chat_profile already exists, no action taken')
else:
    print('Creating chat_profile table')
    cur.execute('''
    CREATE TABLE chat_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        profile TEXT DEFAULT 'default.png',
        province VARCHAR(100),
        municipality VARCHAR(100),
        street VARCHAR(200),
        postal_code VARCHAR(20),
        user_id INTEGER UNIQUE NOT NULL
    );
    ''')
    con.commit()
    print('chat_profile created')
con.close()
