from flask import Flask


def App():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fsqdsdqgsdgsqgqsgqs'
    
    return app
