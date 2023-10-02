import os


class Config:
    """Application configuration class."""

    DEBUG = True
    VIEW_MODE = os.environ.get('VIEW_MODE', 'developer')
    # Add other configurations here
