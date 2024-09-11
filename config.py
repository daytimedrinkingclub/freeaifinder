import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_URL = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'sqlite:///app.db'  # Add a default SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add this line to print the database URI for debugging
    print(f"Database URI: {SQLALCHEMY_DATABASE_URI}")