"""Route declaration."""
from flask import current_app as app
from flask import render_template

import toml
import pathlib
# nav = [
#     {"name": "Home", 'page' : 'home'},
#     {"name": "Short CV", 'page':'cv'},
#     {"name": "Publications", 'page':'pubs'},
#     {"name": "Recipes", 'page':'recipes'},
#     ]
nav = {
    'index': {"name": "Overview",
              'desc': "An overview of the OMW project"},
    'omw1':  {"name": "OMW v1",
              'desc': "The original version linked by PWN"},
    'omw2':  {"name": "OMW v2",
              'desc': 'The new version linked by CILI'},
    'news':  {"name": "News",
              'desc': 'News and Updates'},
    'docs':  {"name": "Documentation",
              'desc': 'Links to some useful documentation'}
}




@app.route("/<page>.html")
def show(page):
    """Show a page"""
    return render_template(
        f"{page}.html",
        page=page,
        nav=nav,
        title=nav[page]['name'],
        description=nav[page]['desc'],
    )


@app.route("/doc/<page>.html")
def show_doc(page):
    """Show a doc page"""
    try:
        with app.open_resource(f'etc/{page}.toml', mode='rt') as f:
            data = toml.loads(f.read())
    except:
        data = dict()
    try:
        with app.open_resource(f'etc/{page}.examples.toml', mode='rt') as f:
            examples = toml.loads(f.read())
    except:
         examples = dict()
      
    return render_template(
        f"doc/{page}.html",
        page=page,
        nav=nav,
        data = data,
        examples = examples,
    )


@app.route("/")
def home():
    """show the home page"""
    return show('index')

