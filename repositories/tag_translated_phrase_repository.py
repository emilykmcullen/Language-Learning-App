from db.run_sql import run_sql
from models.tag_translated_phrase import tagTranslatedPhrase
import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.tag_repository as tag_repository

def save(tag_translated_phrase):
    sql = "INSERT INTO tags_translated_phrases(translated_phrase_id, tag_id) VALUES (%s, %s) RETURNING id"
    values = [tag_translated_phrase.translated_phrase.id, tag_translated_phrase.tag.id]
    results = run_sql(sql, values)
    tag_translated_phrase.id = results[0]['id']
    return tag_translated_phrase

def select_all():
    tag_translated_phrases = []

    sql = "SELECT * FROM tags_translated_phrases"
    results = run_sql(sql)

    for row in results:
        translated_phrase = translated_phrase_repository.select(row['translated_phrase_id'])
        tag = tag_repository.select(row['tag_id'])
        tag_translated_phrase = tagTranslatedPhrase(translated_phrase, tag, row['id'])
        tag_translated_phrases.append(tag_translated_phrase)
    return tag_translated_phrases

def delete_all():
    sql = "DELETE FROM tags_translated_phrases"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags_translated_phrases WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag_translated_phrase):
    sql = "UPDATE tag_translated_phrases SET (translated_phrase_id, tag_id) = (%s, %s) WHERE id = %s"
    values = [tag_translated_phrase.translated_phrase.id, tag_translated_phrase.tag.id, tag_translated_phrase.id]
    run_sql(sql,values)
    
def delete_row(translated_phrase, tag):
    sql = "DELETE FROM tags_translated_phrases WHERE translated_phrase_id = (%s) AND tag_id = (%s)"
    values = [translated_phrase.id, tag.id]
    run_sql(sql, values)

def delete_by_tag_id(id):
    sql = "DELETE FROM tags_translated_phrases WHERE tag_id = (%s)"
    values = [id]
    run_sql(sql, values)
    