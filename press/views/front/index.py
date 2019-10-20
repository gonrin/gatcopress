from gatco import Blueprint
from goblin.server import app
from gatco.response import text
# from goblin.database import db
from goblin.extensions import jinja

@app.route('/')
def index(request):
    #objs = Page.query.filter().limit(10)
    return text("Hello Gonstack")