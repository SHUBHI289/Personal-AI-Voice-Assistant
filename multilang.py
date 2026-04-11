from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel, gettext as _

app = Flask(__name__)
babel = Babel(app)

# Supported languages
LANGUAGES = ['en', 'es', 'fr']

# Configuring translations
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

@babel.localeselector
def get_locale():
    # You can also use request.accept_languages for browser preferences
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
