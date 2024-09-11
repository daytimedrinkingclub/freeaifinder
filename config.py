import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_URL = os.environ.get('DATABASE_URL')
    PRODUCTION_DATABASE_URL = os.environ.get('PRODUCTION_DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = PRODUCTION_DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
heroku git:remote -a freeaifinde
    # Add this line to print the database URI for debugging
    print(f"Database URI: {SQLALCHEMY_DATABASE_URI}")