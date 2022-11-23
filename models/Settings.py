from pydantic import BaseSettings

class AppSettings(BaseSettings):
    HOST: str
    PORT: int
    DEBUG: bool
    SESSION_STORAGE: str
    SESSION_SECRET: str

    class Config:
        env_file= '.env'
        env_file_encoding= 'utf-8'

class JWTSettings(BaseSettings):
    JWT_SECRET: str

    class Config:
        env_file='.env'
        env_file_encoding='utf-8'

