import os


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/identifier.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    VIEW_MODE = os.environ.get('VIEW_MODE', 'developer')