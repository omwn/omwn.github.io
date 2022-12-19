from flask import Flask
from flask_frozen import Freezer
from web import create_app

app = create_app()
app.config.from_pyfile('settings.py')

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
