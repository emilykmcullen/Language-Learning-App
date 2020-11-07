from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.translated_phrase import TranslatedPhrase
import repositories.translated_phrase_repository as translated_phrase_repository

translated_phrases_blueprint = Blueprint("translated_phrases", __name__)

