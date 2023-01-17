##OPEN API STUFF
OPENAI_API_KEY = ''



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "V9CFUwZ4tNyscBa3yFCw4PWbXsqXYfhzdAkHzmzctjr4cL2F"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
