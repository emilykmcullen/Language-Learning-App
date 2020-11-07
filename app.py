from flask import Flask, render_template
from controllers.first_language_phrase_controller import first_language_phrases_blueprint
from controllers.base_controller import base_blueprint

app = Flask(__name__)

app.register_blueprint(first_language_phrases_blueprint)
app.register_blueprint(base_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)