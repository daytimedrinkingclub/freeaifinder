from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Add this import
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize migrate
    
    # Import and register blueprints here, after the app is created
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app