from db.run_sql import run_sql
from models.language import Language

def save(language):
    sql = "INSERT INTO languages(title) VALUES (%s) RETURNING id"
    values = [language.title]
    results = run_sql(sql, values)
    language.id = results[0]['id']
    return language

def select_all():
    languages = []

    sql = "SELECT * FROM languages"
    results = run_sql(sql)
    for row in results:
        language = Language(row['title'], row['id'])
        languages.append(language)
    return languages

def select(id):
    language = None
    sql = "SELECT * FROM languages WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        language = Language(result['title'], result['id'])
    return language

def select_title(title):
    language = None
    sql = "SELECT * FROM languages WHERE title = %s"
    values = [title]
    result = run_sql(sql, values)[0]

    if result is not None:
        language = Language(result['title'], result['id'])
    return language

def delete_all():
    sql = "DELETE FROM languages"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM languages WHERE id = %s"
    values = [id]
    run_sql(sql, values)