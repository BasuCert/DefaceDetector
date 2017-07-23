import os
from app.utils import get_config

class Config(object):
    """Parent configuration class."""
    DEBUG = get_config('DEBUG')
    CSRF_ENABLED = get_config('CSRF_ENABLED')
    SECRET = get_config('SECRET')
    SQLALCHEMY_DATABASE_URI = get_config('DATABASE_URL')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
