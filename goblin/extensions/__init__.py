from .useragent import GatcoUserAgent
from .jinja import Jinja
from ..database import db

jinja = Jinja()

def init_extensions(app):
    GatcoUserAgent.init_app(app)
    jinja.init_app(app)
    