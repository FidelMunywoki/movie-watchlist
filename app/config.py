from logging import DEBUG


class Config:
    '''
    General configuration parent class
    '''
    pass

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