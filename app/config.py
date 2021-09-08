from logging import DEBUG


class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = ' https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
       Config : The parent configuration class with General configurations settings
    '''
    pass
class DevConfig(Config):
    '''
    Developmet configuration child class
    
    Args:
       Config: The parent configuration class with General  configuration setting
    '''
    
    DEBUG = True
    
