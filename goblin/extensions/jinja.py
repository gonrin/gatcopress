from jinja2 import PrefixLoader
from gatco_jinja2 import GatcoJinja2

class Jinja(GatcoJinja2):
    def init_app(self, app, loader=PrefixLoader({}), pkg_name=None, pkg_path=None):
        super(Jinja, self).init_app(app, loader, pkg_name, pkg_path)
        self.add_env("host", app.config.get("HOST", ""))
        self.add_env("static_url", app.config.get("STATIC_URL", ""))

    def add_loader(self, prefix, loader):
        self.env.loader.mapping[prefix] = loader