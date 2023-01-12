from pydantic import BaseSettings


class Settings(BaseSettings):
    connection: str
    class Config:
        env_file = ".env"
settings = Settings()
# import os

# MONGO_USERNAME = os.getenv("MONGO_USERNAME")
# MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")


# MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.bpsdhnh.mongodb.net/Sample"