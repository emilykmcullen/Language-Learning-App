from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.translated_phrase import TranslatedPhrase
import repositories.translated_phrase_repository as translated_phrase_repository

mastered_snaps_blueprint = Blueprint("mastered_snaps_blueprint", __name__)

