class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ('postgresql+psycopg2://'
                               'store:store@localhost:5432/slots')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ERROR_404_HELP = False
    # TOKEN = ...
