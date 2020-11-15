from flask import render_template, request, redirect
from flask import Blueprint
import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.tag_repository as tag_repository
import repositories.tag_translated_phrase_repository as tag_translated_phrase_repository
from models.tag import Tag
import random

base_blueprint = Blueprint("base", __name__)


@base_blueprint.route('/')
def index():
    return render_template('index.html', title='Home')

@base_blueprint.route('/info')
def info():
    return render_template('info.html', title="Info")

@base_blueprint.route('/create_new_tag')
def create_new_tag():
    all_tags = tag_repository.select_all()
    return render_template('create_new_tag.html', title="Create A New Tag", all_tags=all_tags)

# to go to the page to create a new tag
# call the function create_new_tag()
# inside the function select all the tags currently in the databse using tag_repository.select_all()
# and save this list to a variable name all_tags
# the function must return render_template with the parameters of the html page for create_new_tag, the title "Create a New Tag", and the list of tags all_tags

@base_blueprint.route('/create_new_tag/new', methods=["POST"])
def save_created_tag():
    title = request.form['new_tag']
    tag = Tag(title)
    tag_repository.save(tag)
    return redirect('/create_new_tag')

@base_blueprint.route('/create_new_tag/<id>/delete', methods=["POST"])
def delete_tag(id):
    tag_translated_phrase_repository.delete_by_tag_id(id)
    tag_repository.delete(id)
    return redirect('/create_new_tag')
    
@base_blueprint.route('/random')
def play_random():
    all_translated_phrases = translated_phrase_repository.select_all()
    number = len(all_translated_phrases)
    random_number = random.randint(1, number)
    return redirect(f"/sentence_snaps/{random_number}/play")




