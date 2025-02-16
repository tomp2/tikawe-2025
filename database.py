import sqlite3
from pathlib import Path

from flask import g

from config import DATABASE_PATH


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_PATH)

        def make_dicts(cursor, row):
            return dict(
                (cursor.description[idx][0], value) for idx, value in enumerate(row)
            )

        db.row_factory = make_dicts

    return db


if __name__ == "__main__":
    schema = Path("schema.sql").read_text("utf8")
    seed = Path("seed.sql").read_text("utf8")

    with sqlite3.connect(DATABASE_PATH) as conn:
        print("Running schema.sql")
        conn.executescript(schema)
        print("Tables created.")

    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            print("Running seed.sql")
            conn.executescript(seed)
            print("Tables seeded.")
    except sqlite3.IntegrityError as e:
        print(
            f"Failed to seed database due to integrity error. Maybe the database is already seeded?"
        )
        raise e

    print("Database initialized.")
