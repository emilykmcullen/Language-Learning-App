from db.run_sql import run_sql
import repositories.first_language_phrase_repository as first_language_phrase_repository
from models.translated_phrase import TranslatedPhrase

def save(translated_phrase):
    sql = "INSERT INTO translated_phrases(language, phrase, first_language_phrase_id) VALUES ( %s, %s, %s) RETURNING id"
    values = [translated_phrase.language, translated_phrase.phrase, translated_phrase.first_language_phrase.id]
    results = run_sql(sql, values)
    translated_phrase = results[0]['id']
    return translated_phrase

def select_all():
    translated_phrases = []

    sql = "SELECT * FROM translated_phrases"
    results = run_sql(sql)

    for row in results:
        first_language_phrase = first_language_phrase_repository.select(row[first_language_phrase_id])
        translated_phrase = TranslatedPhrase(row['phrase'], row['language'], row['id'], first_language_phrase)
        translated_phrases.append(translated_phrase)
    return translated_phrases

def select_id(id): 
    translated_phrase = None 
    sql = "SELECT * FROM translated_phrases WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        first_language_phrase = first_language_phrase_repository.select(result[first_language_phrase_id])
        translated_phrase = TranslatedPhrase(result['phrase'], result['language'], result['id'], first_language_phrase)
    return translated_phrase

def delete_all():
    sql = "DELETE FROM translated_phrases"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM translated_phrases WHERE id = %s"
    values = [id]
    run_sql(sql, values)
