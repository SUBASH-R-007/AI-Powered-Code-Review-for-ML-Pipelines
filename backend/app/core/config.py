from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str = "./models"
    DATA_PATH: str = "./data"
    
settings = Settings()
