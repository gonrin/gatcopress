from gatco.response import json
from gatco import Blueprint
from jinja2 import Environment, PackageLoader
from goblin.extensions import jinja
from goblin.server import app

admin = Blueprint('admin', url_prefix='/admin')
jinja.add_loader("admin", PackageLoader("goblin.admin", 'templates'))

@admin.route('/')
async def index(request):
    return jinja.render('admin/index.html', request)

@admin.route('/login')
async def login(request):
    return json({'my': 'login'})

@admin.route('/logout')
async def logout(request):
    return json({'my': 'logout'})