from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.first_language_phrase import FirstLanguagePhrase
from models.translated_phrase import TranslatedPhrase
from models.language import Language
import repositories.first_language_phrase_repository as first_language_phrase_repository
import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.language_repository as language_repository
import string

sentence_snaps_blueprint = Blueprint("sentence_snaps_blueprint", __name__ )

@sentence_snaps_blueprint.route("/sentence_snaps")
def sentence_snaps():
    unmastered_translated_phrases = translated_phrase_repository.select_all_unmastered()
    return render_template("sentence_snaps/index.html", unmastered_translated_phrases=unmastered_translated_phrases)

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/delete", methods=["POST"])
def delete_phrase(id):
    first_language_phrase_repository.delete(id)
    return redirect("/sentence_snaps")

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/play")
def play_phrase(id):
    # first_language_phrase = first_language_phrase_repository.select(id)
    translated_phrase = translated_phrase_repository.select(id)
    return render_template("sentence_snaps/play.html", translated_phrase=translated_phrase)

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/edit")
def edit_phrase(id):
    languages = language_repository.select_all()
    translated_phrase = translated_phrase_repository.select(id)
    first_language_phrase = first_language_phrase_repository.select(translated_phrase.first_language_phrase.id)
    return render_template("sentence_snaps/edit.html", first_language_phrase=first_language_phrase, translated_phrase=translated_phrase, languages=languages)

@sentence_snaps_blueprint.route("/sentence_snaps/<id>", methods=['POST'])
def update_phrase(id):
    translated_phrase = translated_phrase_repository.select(id)
    original_first_language_phrase_id = translated_phrase.first_language_phrase.id
    language_input = request.form['language_choice']
    first_language_input = request.form['first_language_input']
    difficulty = request.form['difficulty_choice']
    translated_input = request.form['translated_input']
    language = language_repository.select_title(language_input)
    mastered = True if "mastered" in request.form else False
    new_first_language_phrase = FirstLanguagePhrase(first_language_input, difficulty, original_first_language_phrase_id)
    first_language_phrase_repository.update(new_first_language_phrase)
    new_translated_phrase = TranslatedPhrase(translated_input, language, new_first_language_phrase, mastered, id)
    translated_phrase_repository.update(new_translated_phrase)
    return redirect('/sentence_snaps')
    

@sentence_snaps_blueprint.route("/sentence_snaps/new")
def new_phrase():
    languages = language_repository.select_all()
    return render_template("sentence_snaps/new.html", languages=languages)

@sentence_snaps_blueprint.route("/sentence_snaps", methods=["POST"])
def create_phrase():
    mastered = False
    language_input = request.form['language_choice']
    first_language_input = request.form['first_language_input']
    difficulty = request.form['difficulty_choice']
    translated_input = request.form['translated_input']
    language = language_repository.select_title(language_input)
    first_language_phrase = FirstLanguagePhrase(first_language_input, difficulty)
    first_language_phrase_repository.save(first_language_phrase)
    translated_phrase = TranslatedPhrase(translated_input, language, first_language_phrase, mastered)
    translated_phrase_repository.save(translated_phrase)
    return redirect('/sentence_snaps')

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/results", methods=["POST"])
def results(id):
    translated_phrase = translated_phrase_repository.select(id)
    answer = request.form['answer']
    remove_punctuation_answer = answer.translate(str.maketrans('','', string.punctuation))
    clean_answer = remove_punctuation_answer.lower()
    remove_punctuation_translated_phrase = translated_phrase.phrase.translate(str.maketrans('','',string.punctuation))
    clean_translated_phrase = remove_punctuation_translated_phrase.lower()
    if clean_answer == clean_translated_phrase:
        result = True
    else:
        result = False
    return render_template("sentence_snaps/results.html", result=result, translated_phrase=translated_phrase)


