class Config:
    '''
    General configuration parent class
    '''
    
    GIPHY_API_BASE_URL='https://api.giphy.com/v1/gifs/trending?api_key={}&limit=50&rating=g'
    # GIPHY_API_KEY=''

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