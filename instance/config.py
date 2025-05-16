import os


class BaseConfig:
    """Parent configuration class"""

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APPLICATION_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DevelopmentConfig(BaseConfig):
    """Configurations for Development"""

    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")


APP_CONFIG = {
    "development": DevelopmentConfig,
}
