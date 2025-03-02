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
INSERT INTO users (id, username, password_hash, created_at)
VALUES (7, 'halogeenilamppu', '', '2025-03-02 20:02:09');
INSERT INTO users (id, username, password_hash, created_at)
VALUES (8, 'harava', '', '2025-03-02 20:08:30');
INSERT INTO users (id, username, password_hash, created_at)
VALUES (9, 'pormestari', '', '2025-03-02 20:14:26');
INSERT INTO users (id, username, password_hash, created_at)
VALUES (10, 'minecraft', '', '2025-03-02 20:29:27');


INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (1, 'Classroom Masterpiece', 'Saw this on the whiteboard :D', 'whiteboard',
        '8f783715-5a6a-468d-9d5e-3d1b54ee631e.png', 1, '2025-02-16 21:24:38', 11, 2, '{
    "1f525": 2,
    "1f600": 1
  }', 2);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (2, 'Another one of these', '', 'bathroom', 'cc023aaf-bfdf-4f99-b2e6-cc87cd5bb002.png', 1, '2025-02-16 21:25:15',
        15, 2, '{
    "1f44d": 1,
    "1f611": 3
  }', 3);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (3, 'Yeah.', '', 'hallway', '4086fb8a-b456-40a5-a51b-1ba3bbc6d85d.png', 1, '2025-02-16 21:25:45', 26, 5, '{
  "1f44d": 2,
  "1f525": 2,
  "1f600": 3
}', 2);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (4, 'Tic tac toe', 'Found this on the bathroom mirror', 'bathroom,fun',
        'a7ce09ca-87ca-4579-b4fb-d965601dedf5.png', 1, '2025-02-16 21:30:59', 16, 3, '{
    "1f44d": 1
  }', 5);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (5, 'Bold statement...', '', 'random', '3d9dd75a-6393-4f63-8ba3-785f37bfe2c0.png', 2, '2025-02-16 21:32:11', 30,
        4, '{
    "1f389": 3,
    "1f44d": 5,
    "1f611": 3
  }', 3);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (6, 'bruh', '', 'graffiti', 'f0ab9c41-c04d-49dd-8197-92963f8c9674.png', 3, '2025-02-16 21:33:01', 7, 2, '{}', 0);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (7, 'Sincostan <3', '', 'whiteboard,math', 'd948ce96-0121-42b0-9a75-ca6384e89de4.png', 4, '2025-02-16 21:33:47',
        33, 6, '{
    "1f389": 2,
    "1f44d": 5,
    "1f525": 4,
    "1f600": 3
  }', 4);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (8, 'Ukkeli', 'drew this on my notebook. Pls rate', 'notebook', '7d238146-7a79-4afc-9189-734a2c53658e.png', 6,
        '2025-02-16 21:38:53', 11, 2, '{}', 1);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (9, 'Voi jukran pujut!', 'Ei mul muut', 'whiteboard', 'd5c8a09b-7dbc-4ce6-b268-7dae40cb9d68.png', 7,
        '2025-03-02 20:02:49', 13, 2, '{
    "1f44d": 1
  }', 1);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (10, 'Piirsin tälläse haravan☺️', '', 'notebook', 'c3cdeed1-7c0f-45b7-a37a-84cc134e010b.png', 8,
        '2025-03-02 20:09:57', 12, 1, '{
    "1f44d": 1,
    "1f525": 1
  }', 1);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (11, 'Koht on taas halloween', '', 'fun', '709335b8-2789-465c-b5f2-a1ca8ab49996.png', 9, '2025-03-02 20:14:47',
        4, 0, '{}', 0);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (12, 'creeper💀', '', 'random', '398b8a53-fe4c-43cd-9fbd-3f2d3db8e935.png', 10, '2025-03-02 20:29:53', 7, 0, '{}',
        0);
INSERT INTO doodles (id, title, description, tags, image_url, user_id, created_at, views, likes, reactions, comments)
VALUES (13, 'Enään...', '1. Enään
2. Viellä
3. Jalopeeno', 'fun', '436be5a5-ec28-4560-83a0-e6044eeabf65.png', 10, '2025-03-02 20:33:44', 3, 0, '{}', 0);


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
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (9, 'whiteboard');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (10, 'notebook');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (11, 'fun');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (12, 'random');
INSERT INTO doodle_tags (doodle_id, tag)
VALUES (13, 'fun');


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
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (17, 8, 7, '2025-03-02 20:03:02');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (18, 7, 7, '2025-03-02 20:03:03');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (19, 3, 7, '2025-03-02 20:03:11');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (20, 9, 8, '2025-03-02 20:11:22');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (21, 2, 8, '2025-03-02 20:11:31');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (23, 10, 9, '2025-03-02 20:27:37');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (24, 7, 9, '2025-03-02 20:27:41');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (25, 3, 9, '2025-03-02 20:27:44');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (26, 5, 9, '2025-03-02 20:27:47');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (27, 9, 10, '2025-03-02 20:34:41');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (28, 8, 10, '2025-03-02 20:34:42');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (29, 7, 10, '2025-03-02 20:34:44');
INSERT INTO likes (id, doodle_id, user_id, created_at)
VALUES (30, 4, 10, '2025-03-02 20:34:52');


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
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (18, 5, 7, 'jaahas...', '2025-03-02 20:03:34');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (19, 9, 8, 'no älä muuta sano!', '2025-03-02 20:11:28');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (20, 2, 8, 'moiiii!', '2025-03-02 20:11:35');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (21, 4, 8, 'come on people, im sure they did their best!', '2025-03-02 20:12:41');
INSERT INTO comments (id, doodle_id, user_id, content, created_at)
VALUES (22, 10, 9, 'sopii hyvin raparperinlehtien haravointiin', '2025-03-02 20:27:26');


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
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (30, 3, 7, '👍', '2025-03-02 20:03:12');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (32, 7, 7, '🔥', '2025-03-02 20:03:17');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (33, 7, 7, '🎉', '2025-03-02 20:03:17');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (34, 7, 7, '👍', '2025-03-02 20:03:18');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (35, 7, 7, '😀', '2025-03-02 20:03:18');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (36, 5, 7, '😑', '2025-03-02 20:03:25');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (37, 9, 8, '👍', '2025-03-02 20:11:29');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (38, 2, 8, '👍', '2025-03-02 20:11:36');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (39, 2, 8, '😑', '2025-03-02 20:11:37');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (41, 10, 9, '👍', '2025-03-02 20:27:29');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (42, 10, 9, '🔥', '2025-03-02 20:27:30');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (43, 7, 10, '🔥', '2025-03-02 20:34:45');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (44, 7, 10, '👍', '2025-03-02 20:34:45');
INSERT INTO reactions (id, doodle_id, user_id, emoji, created_at)
VALUES (45, 5, 10, '👍', '2025-03-02 20:34:48');
