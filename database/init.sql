CREATE TABLE IF NOT EXISTS images (
    depth SERIAL PRIMARY KEY,
    image_data BYTEA NOT NULL
);

CREATE INDEX idx_images_depth ON images(depth);
