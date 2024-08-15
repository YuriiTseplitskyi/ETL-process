DELETE FROM "Users"
WHERE domain NOT IN ('example.com', 'example.net', 'example.org');