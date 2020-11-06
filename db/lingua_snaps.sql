DROP TABLE translations;
DROP TABLE phrases;

CREATE TABLE phrases (
    id SERIAL PRIMARY KEY,
    sentence TEXT,
    difficulty VARCHAR
);

CREATE TABLE translations (
    id SERIAL PRIMARY KEY,
    language VARCHAR(255),
    sentence TEXT,
    phrase_id INT REFERENCES phrases(id) ON DELETE CASCADE
);
