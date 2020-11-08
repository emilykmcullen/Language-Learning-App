from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.first_language_phrase import FirstLanguagePhrase
import repositories.first_language_phrase_repository as first_language_phrase_repository
import repositories.language_repository as language_repository

first_language_phrases_blueprint = Blueprint("first_language_phrases", __name__)

@first_language_phrases_blueprint.route("/sentence_snaps")
def sentence_snaps():
    first_language_phrases = first_language_phrase_repository.select_all()
    return render_template("sentence_snaps/index.html", first_language_phrases = first_language_phrases)

@first_language_phrases_blueprint.route("/sentence_snaps/<id>/delete", methods=["POST"])
def delete_phrase(id):
    first_language_phrase_repository.delete(id)
    return redirect("/sentence_snaps")

@first_language_phrases_blueprint.route("/sentence_snaps/<id>/play")
def play_phrase(id):
    first_language_phrase = first_language_phrase_repository.select(id)
    return render_template("sentence_snaps/play.html", first_language_phrase=first_language_phrase)

@first_language_phrases_blueprint.route("/sentence_snaps/<id>/edit")
def edit_phrase(id):
    first_language_phrase = first_language_phrase_repository.select(id)
    return render_template("sentence_snaps/edit.html", first_language_phrase=first_language_phrase)

@first_language_phrases_blueprint.route("/sentence_snaps/new")
def new_phrase():
    languages = language_repository.select_all()
    return render_template("sentence_snaps/new.html", languages=languages)