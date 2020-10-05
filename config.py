import os

class Config:
    '''
    General configuration parent class
    '''
    
    GIPHY_API_BASE_URL='https://api.giphy.com/v1/gifs/trending?api_key={}&limit=50&rating=g'
    # GIPHY_API_KEY=''
    GIPHY_API_KEY = os.environ.get('GIPHY_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/Giphy'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}