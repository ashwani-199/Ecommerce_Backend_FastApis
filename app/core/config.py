from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database Config
    # db_username: str
    # db_password: str
    # db_hostname: str
    # db_port: str
    # db_name: str

    # JWT Config
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()

