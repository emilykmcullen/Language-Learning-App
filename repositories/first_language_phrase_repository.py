from db.run_sql import run_sql
from models.first_language_phrase import FirstLanguagePhrase 

def save(first_language_phrase):
    sql = "INSERT INTO first_language_phrases(phrase, difficulty) VALUES (%s, %s) RETURNING id"
    values = [first_language_phrase.phrase, first_language_phrase.difficulty]
    results = run_sql(sql, values)
    first_language_phrase.id = results[0]['id']
    return first_language_phrase


def select_all():
    first_language_phrases = []

    sql = "SELECT * FROM first_language_phrases"
    results = run_sql(sql)
    for row in results:
        first_language_phrase = FirstLanguagePhrase(row['phrase'], row['difficulty'], row['id'])
        first_language_phrases.append(first_language_phrase)
    return first_language_phrases

def select(id):
    first_language_phrase = None
    sql = "SELECT * FROM first_language_phrases WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        first_language_phrase = FirstLanguagePhrase(result['phrase'], result['difficulty'], result['id'])
    return first_language_phrase

def delete_all():
    sql = "DELETE FROM first_language_phrases"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM first_language_phrases WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(first_language_phrase):
    sql = "UPDATE first_language_phrases SET (phrase, difficulty) = (%s, %s) WHERE id = %s"
    values = [first_language_phrase.phrase, first_language_phrase.difficulty, first_language_phrase.id]
    run_sql(sql,values)