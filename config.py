import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_SERVICE_KEY = os.environ.get('SUPABASE_SERVICE_KEY')