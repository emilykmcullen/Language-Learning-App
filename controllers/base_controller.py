from flask import render_template, request, redirect
from flask import Blueprint
import repositories.tag_repository as tag_repository
import repositories.tag_translated_phrase_repository as tag_translated_phrase_repository
from models.tag import Tag

base_blueprint = Blueprint("base", __name__)


@base_blueprint.route('/')
def index():
    return render_template('index.html', title='Home')

@base_blueprint.route('/create_new_tag')
def create_new_tag():
    all_tags = tag_repository.select_all()
    return render_template('create_new_tag.html', title="Create A New Tag", all_tags=all_tags)

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
    

    