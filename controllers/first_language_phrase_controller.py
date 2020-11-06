from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.first_language_phrase import FirstLanguagePhrase
import repositories.first_language_phrase_repository as first_language_phrase_repository

first_language_phrases_blueprint = Blueprint("first_language_phrases", __name__)

# @first_language_phrases_blueprint()