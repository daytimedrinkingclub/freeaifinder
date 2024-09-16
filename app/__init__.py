from flask import Flask
from config import Config
from supabase import create_client, Client

supabase: Client = None

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    global supabase
    supabase = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_SERVICE_KEY'])

    from app.routes import main
    app.register_blueprint(main.bp)

    return app