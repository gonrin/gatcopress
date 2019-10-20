from goblin.server import app
from goblin.database import db

from goblin.extensions import jinja
from goblin.admin import admin

print("press admin")
@admin.route('/page')
@admin.route('/page/list')
def list(request):
    #objs = Page.query.filter().limit(10)
    return jinja.render('press/admin/page/list.html', request)

@admin.route('/page/create')
@admin.route('/page/edit')
def set(request):
    #objs = Page.query.filter().limit(10)
    return jinja.render('press/admin/page/set.html', request)

@admin.route('/page/get')
def get(request):
    #objs = Page.query.filter().limit(10)
    return jinja.render('press/admin/page/get.html', request)

@admin.route('/page/delete')
def delete(request):
    #objs = Page.query.filter().limit(10)
    return jinja.render('press/admin/page/delete.html', request)