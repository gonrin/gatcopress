import os
import importlib
import pkgutil
from . import app
def resgister_views(urls):
    print(app, urls)
    
    for url in urls:
        module = importlib.import_module(url)


def init_metadata(metadata):
    