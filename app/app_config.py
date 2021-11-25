import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str
    SERVICE_NAME: str
    SERVICE_VERSION: str
    DOMAIN_NAME: str

    BROKER: str
    QUEUE: str
    WORKER_MAX: str

    SENDGRID_API_KEY: str


class ProdConfig(Settings):
    pass


class DevConfig(Settings):
    class Config:
        env_file = "./config/dev.env"


def get_conf():
    if os.getenv("ENV"):
        return ProdConfig()
    else:
        return DevConfig()


conf = get_conf()

if __name__ == "__main__":
    print(conf)
