from db.run_sql import run_sql
from models.tag import Tag
from models.translated_phrase import TranslatedPhrase
from models.language import Language
from models.first_language_phrase import FirstLanguagePhrase
import repositories.language_repository as language_repository
import repositories.first_language_phrase_repository as first_language_phrase_repository

def save(tag):
    sql = "INSERT INTO tags(title) VALUES (%s) RETURNING id"
    values = [tag.title]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['title'], row['id'])
        tags.append(tag)
    return tags

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['title'], result['id'])
    return tag

def select_title(title):
    tag = None
    sql = "SELECT * FROM tags WHERE title = %s"
    values = [title]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['title'], result['id'])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET (title) = (%s) WHERE id = %s"
    values = [tag.title, tag.id]
    run_sql(sql,values)

# this will find and return all the translated phrases that are joined to a particular tag
def translated_phrases(tag):
    translated_phrases = []
    sql = "SELECT translated_phrases.* FROM translated_phrases INNER JOIN tags_translated_phrases ON tags_translated_phrases.translated_phrase_id = translated_phrases.id WHERE tags_translated_phrases.tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)

    for row in results:
        language = language_repository.select(row['language_id'])
        first_language_phrase = first_language_phrase_repository.select(row['first_language_phrase_id'])
        translated_phrase = TranslatedPhrase(row['phrase'], language, first_language_phrase, row['mastered'], row['id'])
        translated_phrases.append(translated_phrase)
    return translated_phrases