""" App entry point. """

from gatco import Gatco
from gatco.sessions import RedisSessionInterface, CookieSessionInterface
from config import Config
#from sanic_cors import CORS, cross_origin

app = Gatco(name=__name__)
app.config.from_object(Config)
app.session_interface = CookieSessionInterface()
app.components = {}

#cors = CORS(app, automatic_options=True)

from .database import init_database
from .extensions import init_extensions
init_database(app)
init_extensions(app)

# static_endpoint = app.config.get("STATIC_URL", None)
# if (static_endpoint is not None) and not ((static_endpoint.startswith( 'http://' ) or (static_endpoint.startswith( 'https://' )))):
#     app.static(static_endpoint, './static')
app.static("/static", './static', name='static')




