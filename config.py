class Config:
    '''
    General configuration parent class
    '''
    
    FOOD_API_BASE_URL ='https://api.nal.usda.gov/fdc/v1/foods/list?api_key={}'

    # https://api.nal.usda.gov/fdc/v1/foods/list?api_key={}

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