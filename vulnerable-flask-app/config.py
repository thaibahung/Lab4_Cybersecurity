import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_USER = os.environ.get('DB_USER') or 'root'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or ''
    DB_NAME = os.environ.get('DB_NAME') or 'vulnerable_db'
    DEBUG = os.environ.get('DEBUG') or True
    ALLOWED_EXTENSIONS = {'txt', 'md', 'py'}  # Example of allowed file types for file inclusion