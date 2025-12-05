import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())

with sqlite3.connect("db.sqlite3") as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Movies (
            Id INTEGER PRIMARY KEY,
            Title TEXT NOT NULL,
            Year INTEGER
        )
    """)

    command = "INSERT OR IGNORE INTO Movies (Id, Title, Year) VALUES (?, ?, ?)"

    for movie in movies:
        try:
            conn.execute(command, (movie["id"], movie["title"], movie["year"]))
            print(f"Inserted: {movie['title']}")
        except sqlite3.IntegrityError as e:
            print(f"Skipped duplicate id {movie['id']}: {e}")

    conn.commit()

print("Done inserting movies.")
