from flask import Flask
from config import Config
from supabase import create_client, Client
import re

supabase: Client = None

def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and underscores)
    and converts spaces to hyphens. Also strips leading and trailing whitespace.
    """
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    global supabase
    supabase = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_SERVICE_KEY'])

    from app.routes import main
    app.register_blueprint(main.bp)

    # Register the Jinja2 filters here
    app.jinja_env.filters['add_utm_params'] = main.add_utm_params
    app.jinja_env.filters['slugify'] = slugify

    return app