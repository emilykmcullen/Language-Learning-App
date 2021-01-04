from db.run_sql import run_sql
import repositories.first_language_phrase_repository as first_language_phrase_repository
import repositories.language_repository as language_repository
from models.translated_phrase import TranslatedPhrase
from models.tag import Tag

def save(translated_phrase):
    sql = "INSERT INTO translated_phrases(language_id, phrase, first_language_phrase_id, mastered) VALUES ( %s, %s, %s, %s) RETURNING id"
    values = [translated_phrase.language.id, translated_phrase.phrase, translated_phrase.first_language_phrase.id, translated_phrase.mastered]
    results = run_sql(sql, values)
    translated_phrase.id = results[0]['id']
    return translated_phrase

def select_all():
    translated_phrases = []

    sql = "SELECT * FROM translated_phrases"
    results = run_sql(sql)

    for row in results:
        first_language_phrase = first_language_phrase_repository.select(row['first_language_phrase_id'])
        language = language_repository.select(row['language_id'])
        translated_phrase = TranslatedPhrase(row['phrase'], language, first_language_phrase, row['mastered'], row['id'])
        translated_phrases.append(translated_phrase)
    return translated_phrases


def select_all_mastered():
    mastered_phrases = []
    sql = "SELECT * FROM translated_phrases WHERE mastered = true"
    results = run_sql(sql)

    for row in results:
        first_language_phrase = first_language_phrase_repository.select(row['first_language_phrase_id'])
        language = language_repository.select(row['language_id'])
        mastered_phrase = TranslatedPhrase(row['phrase'], language, first_language_phrase, row['mastered'], row['id'])
        mastered_phrases.append(mastered_phrase)
    return mastered_phrases

def select_all_unmastered():
    unmastered_phrases = []
    sql = "SELECT * FROM translated_phrases WHERE mastered = false"
    results = run_sql(sql)

    for row in results:
        first_language_phrase = first_language_phrase_repository.select(row['first_language_phrase_id'])
        language = language_repository.select(row['language_id'])
        unmastered_phrase = TranslatedPhrase(row['phrase'], language, first_language_phrase, row['mastered'], row['id'])
        unmastered_phrases.append(unmastered_phrase)
    return unmastered_phrases

def select(id): 
    translated_phrase = None 
    sql = "SELECT * FROM translated_phrases WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        first_language_phrase = first_language_phrase_repository.select(result['first_language_phrase_id'])
        language = language_repository.select(result['language_id'])
        translated_phrase = TranslatedPhrase(result['phrase'], language, first_language_phrase, result['mastered'], result['id'])
    return translated_phrase

def select_by_language(id):
    phrases_by_language = []
    sql = "SELECT * FROM translated_phrases WHERE language_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        first_language_phrase = first_language_phrase_repository.select(row['first_language_phrase_id'])
        language = language_repository.select(row['language_id'])
        phrase = TranslatedPhrase(row['phrase'], language, first_language_phrase, row['mastered'], row['id'])
        phrases_by_language.append(phrase)
    return phrases_by_language

def list_all_ids():
    ids = []
    sql = "SELECT id FROM translated_phrases"
    results = run_sql(sql)

    for row in results:
        row_id = row['id']
        ids.append(row_id)
    return ids

def delete_all():
    sql = "DELETE FROM translated_phrases"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM translated_phrases WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_by_language(language_id):
    sql = "DELETE FROM translated_phrases WHERE language_id = %s "
    values = [language_id]
    run_sql(sql,values)


def update(translated_phrase):
    sql = "UPDATE translated_phrases SET (language_id, phrase, first_language_phrase_id, mastered) = (%s, %s, %s, %s) WHERE id = %s"
    values = [translated_phrase.language.id, translated_phrase.phrase, translated_phrase.first_language_phrase.id, translated_phrase.mastered, translated_phrase.id]
    run_sql(sql,values)

# this will return all the tags that are joined to a specific phrase
def tags(translated_phrase):
    tags = []
    sql = "SELECT tags.* FROM tags INNER JOIN tags_translated_phrases ON tags_translated_phrases.tag_id = tags.id WHERE tags_translated_phrases.translated_phrase_id = %s"
    values = [translated_phrase.id]
    results = run_sql(sql, values)
    for row in results:
        tag = Tag(row['title'], row['id'])
        tags.append(tag)
    return tags

def tag_titles(translated_phrase):
    tag_titles = []
    sql = "SELECT tags.* FROM tags INNER JOIN tags_translated_phrases ON tags_translated_phrases.tag_id = tags.id WHERE tags_translated_phrases.translated_phrase_id = %s"
    values = [translated_phrase.id]
    results = run_sql(sql, values)
    for row in results:
        tag_title = (row['title'])
        tag_titles.append(tag_title)
    return tag_titles
