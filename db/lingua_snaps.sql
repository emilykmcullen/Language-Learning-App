DROP TABLE translated_phrases;
DROP TABLE first_language_phrases;
DROP TABLE languages;

CREATE TABLE languages (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255)
);

CREATE TABLE first_language_phrases (
    id SERIAL PRIMARY KEY,
    phrase TEXT,
    difficulty VARCHAR
);

CREATE TABLE translated_phrases (
    id SERIAL PRIMARY KEY,
    language_id INT REFERENCES languages(id) ON DELETE CASCADE,
    phrase TEXT,
    first_language_phrase_id INT REFERENCES first_language_phrases(id) ON DELETE CASCADE
);



-- make a Language class, repository, controller, make any necessary changes to translated phrase objects elsewhere