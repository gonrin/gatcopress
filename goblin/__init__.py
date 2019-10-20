import os
import importlib
import pkgutil
import ujson
from jinja2 import PackageLoader
from .server import app
from goblin.extensions import jinja

#from .urls import resgister_views

def register_component(name):
    with open(name + '/metadata.json', 'r') as metadata:
        metadata = ujson.load(metadata)

        #views
        viewurls = metadata.get("views", [])
        for url in viewurls:
            module = importlib.import_module(".".join([name, url]))

        #templates
        templateurls = metadata.get("templates", "templates")
        jinja.add_loader(name, PackageLoader(name, templateurls))

        app.components["name"] = name

def init_admin():
    from .admin import admin
    app.blueprint(admin)

def run_app(host="127.0.0.1", port=8000, config=None, debug=False, workers=os.cpu_count()):
    """ Function for bootstrapping gatco app. """
    init_admin()
    app.run(host=host, port=port, debug=debug, workers=workers)