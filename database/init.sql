DROP TABLE IF EXISTS images;

CREATE TABLE images (
    depth SERIAL PRIMARY KEY,
    data INTEGER[]
);
