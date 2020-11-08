from db.run_sql import run_sql
import repositories.first_language_phrase_repository as first_language_phrase_repository
import repositories.language_repository as language_repository
from models.translated_phrase import TranslatedPhrase

def save(translated_phrase):
    sql = "INSERT INTO translated_phrases(language_id, phrase, first_language_phrase_id) VALUES ( %s, %s, %s) RETURNING id"
    values = [translated_phrase.language.id, translated_phrase.phrase, translated_phrase.first_language_phrase.id]
    results = run_sql(sql, values)
    translated_phrase = results[0]['id']
    return translated_phrase

def select_all():
    translated_phrases = []

    sql = "SELECT * FROM translated_phrases"
    results = run_sql(sql)

    for row in results:
        first_language_phrase = first_language_phrase_repository.select(row[first_language_phrase_id])
        language = language_repository.select(row[language_id])
        translated_phrase = TranslatedPhrase(row['phrase'], language, first_language_phrase, row['id'])
        translated_phrases.append(translated_phrase)
    return translated_phrases

def select_id(id): 
    translated_phrase = None 
    sql = "SELECT * FROM translated_phrases WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        first_language_phrase = first_language_phrase_repository.select(result[first_language_phrase_id])
        language = language_repository.select(result[language_id])
        translated_phrase = TranslatedPhrase(result['phrase'], language, first_language_phrase, result['id'])
    return translated_phrase

def delete_all():
    sql = "DELETE FROM translated_phrases"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM translated_phrases WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(translated_phrase):
    sql = "UPDATE translated_phrases SET (language_id, phrase, first_language_phrase_id) = (%s, %s, %s) WHERE id = %s"
    values = [translated_phrase.language.id, translated_phrase.difficulty, translated_phrase.first_language_phrase.id, translated_phrase.id]
    run_sql(sql,values)