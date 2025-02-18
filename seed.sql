INSERT INTO users (id, username, password_hash, created_at)
VALUES (1, 'Appleman', '', '2025-02-16 21:23:59');
INSERT INTO users (id, username, password_hash, created_at)
VALUES (2, 'Patonki', '', '2025-02-16 21:31:14');
INSERT INTO users (id, username, password_hash, created_at)
VALUES (3, 'asdf', '', '2025-02-16 21:32:41');
INSERT INTO users (id, username, password_hash, created_at)
VALUES (4, 'Pepsi max', '', '2025-02-16 21:33:27');
INSERT INTO users (id, username, password_hash, created_at)
VALUES (5, 'osajoukko', '', '2025-02-16 21:36:35');
INSERT INTO users (id, username, password_hash, created_at)
VALUES (6, 'apow9e4hgaiu', '', '2025-02-16 21:38:23');

INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (1, 'Classroom Masterpiece', 'Saw this on the whiteboard :D', 'whiteboard',
        '8f783715-5a6a-468d-9d5e-3d1b54ee631e.png', 1, '2025-02-16 21:24:38', 10, 2, '{
    "1f525": 2,
    "1f600": 1
  }', 2);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (2, 'Another one of these', '', 'bathroom', 'cc023aaf-bfdf-4f99-b2e6-cc87cd5bb002.png', 1, '2025-02-16 21:25:15',
        9, 1, '{
    "1f611": 2
  }', 2);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (3, 'Yeah.', '', 'hallway', '4086fb8a-b456-40a5-a51b-1ba3bbc6d85d.png', 1, '2025-02-16 21:25:45', 21, 3, '{
  "1f44d": 1,
  "1f525": 2,
  "1f600": 3
}', 2);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (4, 'Tic tac toe', 'Found this on the bathroom mirror', 'bathroom,fun',
        'a7ce09ca-87ca-4579-b4fb-d965601dedf5.png', 1, '2025-02-16 21:30:59', 11, 2, '{
    "1f44d": 1
  }', 4);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (5, 'Bold statement...', '', 'random', '3d9dd75a-6393-4f63-8ba3-785f37bfe2c0.png', 2, '2025-02-16 21:32:11', 18,
        3, '{
    "1f389": 3,
    "1f44d": 4,
    "1f611": 2
  }', 2);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (6, 'bruh', '', 'graffiti', 'f0ab9c41-c04d-49dd-8197-92963f8c9674.png', 3, '2025-02-16 21:33:01', 5, 2, '{}', 0);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (7, 'Sincostan <3', '', 'whiteboard,math', 'd948ce96-0121-42b0-9a75-ca6384e89de4.png', 4, '2025-02-16 21:33:47',
        20, 3, '{
    "1f389": 1,
    "1f44d": 3,
    "1f525": 2,
    "1f600": 2
  }', 4);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (8, 'Ukkeli', 'drew this on my notebook. Pls rate', 'notebook', '7d238146-7a79-4afc-9189-734a2c53658e.png', 6,
        '2025-02-16 21:38:53', 3, 0, '{}', 1);

INSERT INTO doodle_tags (doodle_id, tag)
VALUES (1, 'whiteboard');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (2, 'bathroom');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (3, 'hallway');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (4, 'bathroom');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (4, 'fun');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (5, 'random');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (6, 'graffiti');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (7, 'whiteboard');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (7, 'math');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (8, 'notebook');

INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (1, 4, 2, 'Nice', '2025-02-16 21:31:22');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (2, 1, 2, 'i saw this too :D', '2025-02-16 21:31:37');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (3, 3, 2, 'Makes me feel hunger', '2025-02-16 21:32:33');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (4, 1, 4, ':DDDD', '2025-02-16 21:33:58');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (5, 2, 4, 'mo', '2025-02-16 21:34:12');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (6, 4, 4, 'what an idiot', '2025-02-16 21:34:30');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (7, 4, 4, 'the x player is idiot', '2025-02-16 21:34:38');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (8, 7, 4, 'Forgot to add: saw this at the place where i initially saw this. It just was there idk how.',
        '2025-02-16 21:35:28');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (9, 7, 5, 'Sin tas con!', '2025-02-16 21:36:56');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (10, 5, 5, 'Someone has guts!', '2025-02-16 21:37:11');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (11, 3, 5, 'I have one baguette on me right now. Eating it right now.', '2025-02-16 21:37:30');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (12, 2, 5, '? is this?', '2025-02-16 21:37:56');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (13, 7, 6, 'love sincostan', '2025-02-16 21:39:40');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (14, 8, 1, 'idk man, this is not that cool', '2025-02-16 21:41:25');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (15, 7, 1, '<3', '2025-02-16 21:41:56');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (16, 4, 1, 'agree with pepis max', '2025-02-16 21:42:20');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (17, 5, 1, 'yeah...', '2025-02-16 21:42:49');

INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (1, 4, 2, '2025-02-16 21:31:26');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (2, 1, 2, '2025-02-16 21:31:29');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (3, 2, 4, '2025-02-16 21:34:17');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (4, 3, 4, '2025-02-16 21:34:19');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (5, 4, 4, '2025-02-16 21:34:22');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (6, 5, 4, '2025-02-16 21:35:36');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (7, 1, 4, '2025-02-16 21:35:50');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (8, 7, 5, '2025-02-16 21:36:41');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (9, 6, 5, '2025-02-16 21:36:59');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (10, 3, 5, '2025-02-16 21:37:34');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (11, 7, 6, '2025-02-16 21:39:31');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (12, 5, 6, '2025-02-16 21:39:48');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (13, 3, 6, '2025-02-16 21:39:55');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (14, 7, 1, '2025-02-16 21:41:57');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (15, 6, 1, '2025-02-16 21:42:00');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (16, 5, 1, '2025-02-16 21:42:30');

INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (1, 4, 2, '👍', '2025-02-16 21:31:19');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (2, 1, 2, '🔥', '2025-02-16 21:31:42');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (3, 3, 2, '😀', '2025-02-16 21:32:20');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (4, 1, 4, '🔥', '2025-02-16 21:33:51');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (5, 1, 4, '😀', '2025-02-16 21:33:55');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (6, 2, 4, '😑', '2025-02-16 21:34:16');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (7, 5, 4, '👍', '2025-02-16 21:35:35');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (8, 7, 5, '👍', '2025-02-16 21:36:42');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (9, 5, 5, '🎉', '2025-02-16 21:37:13');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (10, 5, 5, '👍', '2025-02-16 21:37:13');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (11, 3, 5, '😀', '2025-02-16 21:37:31');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (12, 3, 5, '🔥', '2025-02-16 21:37:34');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (13, 2, 5, '😑', '2025-02-16 21:37:50');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (14, 7, 6, '👍', '2025-02-16 21:39:26');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (15, 7, 6, '😀', '2025-02-16 21:39:28');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (16, 7, 6, '🔥', '2025-02-16 21:39:29');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (17, 5, 6, '🎉', '2025-02-16 21:39:47');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (18, 5, 6, '👍', '2025-02-16 21:39:48');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (19, 5, 6, '😑', '2025-02-16 21:39:53');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (20, 3, 6, '👍', '2025-02-16 21:39:57');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (21, 3, 6, '🔥', '2025-02-16 21:39:58');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (22, 3, 6, '😀', '2025-02-16 21:40:02');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (23, 7, 1, '👍', '2025-02-16 21:41:43');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (24, 7, 1, '🔥', '2025-02-16 21:41:43');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (25, 7, 1, '😀', '2025-02-16 21:41:44');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (26, 7, 1, '🎉', '2025-02-16 21:41:46');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (27, 5, 1, '🎉', '2025-02-16 21:42:35');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (28, 5, 1, '👍', '2025-02-16 21:42:36');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (29, 5, 1, '😑', '2025-02-16 21:42:36');
