from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.language import Language
import repositories.language_repository as language_repository
import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.tag_translated_phrase_repository as tag_translated_phrase_repository

language_blueprint = Blueprint("language_blueprint", __name__)

@language_blueprint.route('/add_new_language')
def add_new_language():
    all_languages = language_repository.select_all()
    return render_template('new_languages/new_language.html', all_languages=all_languages)

@language_blueprint.route('/add_new_language/new', methods=['POST'])
def create_new_language():
    title = request.form['new_language']
    language = Language(title)
    language_repository.save(language)
    return redirect('/add_new_language')

@language_blueprint.route('/add_new_language/<id>/delete', methods=["POST"])
def delete_language(id):
    translated_phrases = translated_phrase_repository.select_by_language(id)
    for translated_phrase in translated_phrases:
        tag_translated_phrase_repository.delete_by_translated_phrase(translated_phrase)
    translated_phrase_repository.delete_by_language(id)
    language_repository.delete(id)
    return redirect('/add_new_language')