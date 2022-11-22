from pydantic import BaseSettings

class Settings(BaseSettings):
    IP_M1     : str = 'localhost'
    PORT_M1  : str = '3000'
    IP_M2     : str = 'localhost'
    PORT_M2  : str = '3001'

settings = Settings()
