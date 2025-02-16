import sqlite3

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
