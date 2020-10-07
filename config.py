import os
import cloudinary

class Config:
    '''
    General configuration parent class
    '''
    
    GIPHY_API_BASE_URL='https://api.giphy.com/v1/gifs/trending?api_key={}&limit=50&rating=g'
    # GIPHY_API_KEY=''
    GIPHY_API_KEY = os.environ.get('GIPHY_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kate:Kanini12@localhost/giphy'

    SQLALCHEMY_TRACK_MODIFICATIONS=False   

    UPLOADED_PHOTOS_DEST ='app/static/photos' 

    cloudinary.config(cloud_name='dew5ge1ch', api_key='361751723152852', api_secret='l2VlpcjUV6Nk9Gh9qi5UCwqDyZ4')


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kate:Kanini12@localhost/giphy'
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}