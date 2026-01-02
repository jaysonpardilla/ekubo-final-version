import sqlite3
import sys

DB='db.sqlite3'
try:
    con=sqlite3.connect(DB)
    cur=con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    print('tables:')
    for r in cur.fetchall():
        print(' -', r[0])
    print('\n--- django_migrations rows for chat ---')
    try:
        cur.execute("SELECT id, app, name, applied FROM django_migrations WHERE app='chat'")
        for r in cur.fetchall():
            print(r)
    except Exception as e:
        print('Could not query django_migrations:', e)
    con.close()
except Exception as e:
    print('Error connecting to', DB, e)
    sys.exit(1)
