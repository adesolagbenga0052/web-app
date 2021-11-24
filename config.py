"""Flask configuration."""
from os import environ, path
basedir = path.abspath(path.dirname(__file__))


class Config:
    """Base config."""
    SECRET_KEY = "qsZ5srBF9-j3tgdMsd11hdbg2VLUyKQYqWFQ1EZyKI6PDVVTLXduxWoM1N0wESR0zFvSPFDs9ogpMjgl9wFxXw"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI ="sqlite:///databank.sqlite" 
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db" 
    SQLALCHEMY_TRACK_MODIFICATIONS = True