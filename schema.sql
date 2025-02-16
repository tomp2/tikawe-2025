CREATE TABLE IF NOT EXISTS users
(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT UNIQUE NOT NULL,
    password_hash TEXT        NOT NULL,
    created_at    TEXT        NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tags
(
    name TEXT UNIQUE NOT NULL PRIMARY KEY
);

INSERT INTO tags (name)
VALUES ('whiteboard'),
       ('bathroom'),
       ('notebook'),
       ('table'),
       ('art'),
       ('random'),
       ('sketch'),
       ('fun'),
       ('math'),
       ('graffiti'),
       ('hallway');

CREATE TABLE IF NOT EXISTS doodle_tags
(
    doodle_id INTEGER NOT NULL,
    tag       INTEGER NOT NULL,
    PRIMARY KEY (doodle_id, tag),
    FOREIGN KEY (doodle_id) REFERENCES doodles (id),
    FOREIGN KEY (tag) REFERENCES tags (name)
);


CREATE TABLE IF NOT EXISTS doodles
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    description TEXT    NOT NULL,
    tags        TEXT    NOT NULL,
    image_url   TEXT    NOT NULL,
    user_id     INTEGER NOT NULL,
    created_at  TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    views       INTEGER          DEFAULT 0,
    likes       INTEGER          DEFAULT 0,
    reactions   JSON             DEFAULT '{}',
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS comments
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    doodle_id  INTEGER NOT NULL,
    user_id    INTEGER NOT NULL,
    content    TEXT    NOT NULL,
    created_at TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (doodle_id) REFERENCES doodles (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS likes
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    doodle_id  INTEGER NOT NULL,
    user_id    INTEGER NOT NULL,
    created_at TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (doodle_id, user_id),
    FOREIGN KEY (doodle_id) REFERENCES doodles (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS views
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    doodle_id INTEGER NOT NULL,
    user_id   INTEGER,
    viewed_at TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (doodle_id) REFERENCES doodles (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);


CREATE TABLE IF NOT EXISTS reactions
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    doodle_id  INTEGER NOT NULL,
    user_id    INTEGER NOT NULL,
    emoji      TEXT    NOT NULL,
    created_at TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (doodle_id, user_id, emoji),
    FOREIGN KEY (doodle_id) REFERENCES doodles (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
