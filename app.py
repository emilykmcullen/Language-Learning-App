from flask import Flask, render_template
from controllers.sentence_snaps_controller import sentence_snaps_blueprint
from controllers.mastered_snaps_controller import mastered_snaps_blueprint
from controllers.base_controller import base_blueprint
from controllers.languages_controller import language_blueprint

app = Flask(__name__)

app.register_blueprint(sentence_snaps_blueprint)
app.register_blueprint(mastered_snaps_blueprint)
app.register_blueprint(base_blueprint)
app.register_blueprint(language_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


