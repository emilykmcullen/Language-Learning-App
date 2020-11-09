from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.translated_phrase import TranslatedPhrase
from models.first_language_phrase import FirstLanguagePhrase
from models.language import Language
import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.first_language_phrase_repository as first_language_phrase_repository
import repositories.language_repository as language_repository
import string

mastered_snaps_blueprint = Blueprint("mastered_snaps_blueprint", __name__)

@mastered_snaps_blueprint.route("/mastered_snaps")
def mastered_snaps():
    mastered_translated_phrases = translated_phrase_repository.select_all_mastered()
    return render_template("mastered_snaps/index.html",  mastered_translated_phrases=mastered_translated_phrases)

@mastered_snaps_blueprint.route("/mastered_snaps/<id>/delete", methods=["POST"])
def delete_phrase(id):
    translated_phrase_repository.delete(id)
    return redirect("/mastered_snaps")

@mastered_snaps_blueprint.route("/mastered_snaps/<id>/play")
def play_phrase(id):
    translated_phrase = translated_phrase_repository.select(id)
    return render_template("mastered_snaps/play.html", translated_phrase=translated_phrase)

@mastered_snaps_blueprint.route("/mastered_snaps/<id>/edit")
def edit_phrase(id):
    languages = language_repository.select_all()
    translated_phrase = translated_phrase_repository.select(id)
    first_language_phrase = first_language_phrase_repository.select(translated_phrase.first_language_phrase.id)
    return render_template("mastered_snaps/edit.html", languages=languages, translated_phrase=translated_phrase, first_language_phrase=first_language_phrase)

@mastered_snaps_blueprint.route("/mastered_snaps/<id>", methods=['POST'])
def update_phrase(id):
    translated_phrase = translated_phrase_repository.select(id)
    original_first_language_phrase_id = translated_phrase.first_language_phrase.id
    language_input = request.form['language_choice']
    first_language_input = request.form['first_language_input']
    difficulty = request.form['difficulty_choice']
    translated_input = request.form['translated_input']
    language = language_repository.select_title(language_input)
    mastered = False if "mastered" in request.form else True
    new_first_language_phrase = FirstLanguagePhrase(first_language_input, difficulty, original_first_language_phrase_id)
    first_language_phrase_repository.update(new_first_language_phrase)
    new_translated_phrase = TranslatedPhrase(translated_input, language, new_first_language_phrase, mastered, id)
    translated_phrase_repository.update(new_translated_phrase)
    return redirect('/mastered_snaps')

@mastered_snaps_blueprint.route("/mastered_snaps/<id>/results", methods=["POST"])
def results(id):
    translated_phrase = translated_phrase_repository.select(id)
    answer = request.form['answer']
    remove_punctuation_answer = answer.translate(str.maketrans('','', string.punctuation))
    clean_answer = remove_punctuation_answer.lower()
    remove_punctuation_translated_phrase = translated_phrase.phrase.translate(str.maketrans('','',string.punctuation))
    clean_translated_phrase = remove_punctuation_translated_phrase.lower()
    id = id
    if clean_answer == clean_translated_phrase:
        result = True
    else:
        result = False
    return render_template("mastered_snaps/results.html", result=result, translated_phrase=translated_phrase, answer=answer, id=id)

@mastered_snaps_blueprint.route("/mastered_snaps/<id>/update_mastered", methods=["POST"])
def update_mastered(id):
    translated_phrase = translated_phrase_repository.select(id)
    phrase = translated_phrase.phrase
    language = translated_phrase.language
    first_language_phrase = translated_phrase.first_language_phrase
    mastered = False
    new_translated_phrase = TranslatedPhrase(phrase, language, first_language_phrase, mastered, id)
    translated_phrase_repository.update(new_translated_phrase)
    return redirect('/mastered_snaps')

@mastered_snaps_blueprint.route("/mastered_snaps/<id>/show_answer")
def show_answer(id):
    translated_phrase = translated_phrase_repository.select(id)
    return render_template("mastered_snaps/show_answer.html", translated_phrase=translated_phrase)