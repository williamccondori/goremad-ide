from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    MONGODB_URL_BASE_DATOS: str
    MONGODB_NOMBRE_BASE_DATOS: str

    ORIGENES_PERMITIDOS: str

    MAPBOX_TOKEN: str

    GEOSERVER_URL: str
    GEOSERVER_USER: str
    GEOSERVER_PASSWORD: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
