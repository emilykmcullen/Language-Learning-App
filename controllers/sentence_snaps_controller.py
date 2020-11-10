from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag_translated_phrase import tagTranslatedPhrase
from models.first_language_phrase import FirstLanguagePhrase
from models.translated_phrase import TranslatedPhrase
from models.language import Language
import repositories.first_language_phrase_repository as first_language_phrase_repository
import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.language_repository as language_repository
import repositories.tag_repository as tag_repository
import repositories.tag_translated_phrase_repository as tag_translated_phrase_repository

import string

sentence_snaps_blueprint = Blueprint("sentence_snaps_blueprint", __name__ )

@sentence_snaps_blueprint.route("/sentence_snaps")
def sentence_snaps():
    all_tags = tag_repository.select_all()
    unmastered_translated_phrases = translated_phrase_repository.select_all_unmastered()
    tag_translated_phrases = tag_translated_phrase_repository.select_all()
    return render_template("sentence_snaps/index.html", unmastered_translated_phrases=unmastered_translated_phrases, tag_translated_phrases=tag_translated_phrases, all_tags=all_tags)

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/delete", methods=["POST"])
def delete_phrase(id):
    translated_phrase_repository.delete(id)
    return redirect("/sentence_snaps")

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/play")
def play_phrase(id):
    translated_phrase = translated_phrase_repository.select(id)
    return render_template("sentence_snaps/play.html", translated_phrase=translated_phrase)

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/edit")
def edit_phrase(id):
    tag_translated_phrases = tag_translated_phrase_repository.select_all()
    all_tags = tag_repository.select_all()
    languages = language_repository.select_all()
    translated_phrase = translated_phrase_repository.select(id)
    tag_titles = translated_phrase_repository.tag_titles(translated_phrase)
    first_language_phrase = first_language_phrase_repository.select(translated_phrase.first_language_phrase.id)
    return render_template("sentence_snaps/edit.html", first_language_phrase=first_language_phrase, translated_phrase=translated_phrase, languages=languages, all_tags=all_tags, tag_translated_phrases=tag_translated_phrases, tag_titles=tag_titles)

@sentence_snaps_blueprint.route("/sentence_snaps/<id>", methods=['POST'])
def update_phrase(id):
    translated_phrase = translated_phrase_repository.select(id)
    original_first_language_phrase_id = translated_phrase.first_language_phrase.id
    language = language_repository.select_title(request.form['language_choice'])
    first_language_input = request.form['first_language_input']
    difficulty = request.form['difficulty_choice']
    translated_input = request.form['translated_input']
    mastered = True if "mastered" in request.form else False
    new_first_language_phrase = FirstLanguagePhrase(first_language_input, difficulty, original_first_language_phrase_id)
    first_language_phrase_repository.update(new_first_language_phrase)
    # first language phrase is updated now
    new_translated_phrase = TranslatedPhrase(translated_input, language, new_first_language_phrase, mastered, id)
    translated_phrase_repository.update(new_translated_phrase)
    # translated phrase is updated
    #REMOVE TAGS
    if request.form['remove_tags'] != 'none':
        tag_to_remove = tag_repository.select_title(request.form['remove_tags'])
        tag_translated_phrase_repository.delete_row(new_translated_phrase, tag_to_remove)
        print("Hello blablabal")
    #ADD TAGS
    if request.form['tags'] != 'none':
        new_tag = tag_repository.select_title(request.form['tags'])
        tag_translated_phrase = tagTranslatedPhrase(new_translated_phrase, new_tag)
        tag_translated_phrase_repository.save(tag_translated_phrase)
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
    id = id
    if clean_answer == clean_translated_phrase:
        result = True
    else:
        result = False
    return render_template("sentence_snaps/results.html", result=result, translated_phrase=translated_phrase, answer=answer, id=id)

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/update_mastered", methods=["POST"])
def update_mastered(id):
    translated_phrase = translated_phrase_repository.select(id)
    phrase = translated_phrase.phrase
    language = translated_phrase.language
    first_language_phrase = translated_phrase.first_language_phrase
    mastered = True
    new_translated_phrase = TranslatedPhrase(phrase, language, first_language_phrase, mastered, id)
    translated_phrase_repository.update(new_translated_phrase)
    return redirect('/sentence_snaps')

@sentence_snaps_blueprint.route("/sentence_snaps/<id>/show_answer")
def show_answer(id):
    translated_phrase = translated_phrase_repository.select(id)
    return render_template("/sentence_snaps/show_answer.html", translated_phrase=translated_phrase)

@sentence_snaps_blueprint.route("/sentence_snaps/filter", methods=["POST"])
def filter_snaps():
    tags_translated_phrases = tag_translated_phrase_repository.select_all()
    all_tags = tag_repository.select_all()
    tag = tag_repository.select_title(request.form['tag_choice'])
    print(tag.title)
    unmastered_translated_phrases = tag_repository.translated_phrases(tag)
    print(unmastered_translated_phrases[0])
    return render_template("sentence_snaps/filtered.html", tag=tag, tags_translated_phrases=tags_translated_phrases, all_tags=all_tags, unmastered_translated_phrases=unmastered_translated_phrases)




