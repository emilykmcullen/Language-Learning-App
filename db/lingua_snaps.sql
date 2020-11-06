DROP TABLE translated_phrases;
DROP TABLE first_language_phrases;

CREATE TABLE first_language_phrases (
    id SERIAL PRIMARY KEY,
    phrase TEXT,
    difficulty VARCHAR
);

CREATE TABLE translated_phrases (
    id SERIAL PRIMARY KEY,
    language VARCHAR(255),
    phrase TEXT,
    first_language_phrase_id INT REFERENCES first_language_phrases(id) ON DELETE CASCADE
);
