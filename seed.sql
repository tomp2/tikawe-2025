INSERT INTO users (username, password_hash)
VALUES ('user1', ''),
       ('user2', ''),
       ('user3', '');

INSERT INTO doodles (title, description, tags, image_url, user_id, created_at, views, likes, reactions)
VALUES ('Classroom Masterpiece', 'A doodle drawn on the classroom whiteboard during math class.',
        'whiteboard, math, fun', 'example1.jpg', 1, '2025-01-14T10:00:00', 15, 3, '{"👍": 2, "😂": 1}'),
       ('Notebook Scribble', 'A random sketch from my notebook during a boring lecture.', 'notebook, sketch, random',
        'example2.jpg', 2, '2025-01-13T15:30:00', 25, 5, '{"👍": 4, "😮": 1}'),
       ('Bathroom Graffiti', 'Some artistic graffiti I saw on a bathroom stall door.', 'graffiti, bathroom, art',
        'example3.jpg', 3, '2025-01-12T20:00:00', 30, 10, '{"👍": 8, "😂": 2}');

INSERT INTO comments (doodle_id, user_id, content, created_at)
VALUES (1, 2, 'This is hilarious! Math class will never be the same.', '2025-01-14T10:15:00'),
       (1, 3, 'Looks like someone had fun with algebra!', '2025-01-14T10:20:00'),
       (2, 1, 'I do the same in my notebook! Great job.', '2025-01-13T16:00:00'),
       (3, 1, 'This is some next-level bathroom art.', '2025-01-12T21:00:00');

INSERT INTO likes (doodle_id, user_id, created_at)
VALUES (1, 2, '2025-01-14T10:05:00'),
       (1, 3, '2025-01-14T10:06:00'),
       (2, 1, '2025-01-13T16:10:00'),
       (3, 1, '2025-01-12T21:05:00'),
       (3, 2, '2025-01-12T21:10:00');

INSERT INTO views (doodle_id, user_id, viewed_at)
VALUES (1, 2, '2025-01-14T10:02:00'),
       (1, 3, '2025-01-14T10:03:00'),
       (2, 1, '2025-01-13T16:05:00'),
       (3, 1, '2025-01-12T21:01:00'),
       (3, 2, '2025-01-12T21:02:00');

INSERT INTO reactions (doodle_id, user_id, emoji, created_at)
VALUES (1, 2, '👍', '2025-01-14T10:07:00'),
       (1, 3, '😂', '2025-01-14T10:08:00'),
       (2, 1, '👍', '2025-01-13T16:15:00'),
       (3, 1, '👍', '2025-01-12T21:15:00'),
       (3, 2, '😂', '2025-01-12T21:16:00');
