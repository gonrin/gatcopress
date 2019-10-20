from gatco import Blueprint
from goblin.server import app
# from goblin.database import db
from goblin.extensions import jinja

@app.route('/page/get')
def index(request):
    #objs = Page.query.filter().limit(10)
    return jinja.render('press/front/page/get.html', request)