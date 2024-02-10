from pydantic import BaseModel
from functools import lru_cache

class Settings(BaseModel):
    env_name: str = "dev"
    base_url: str = "http://localhost:8000"
    api_key: str = "e1c4d6158ecc354e82905ebafe1d530f"

@lru_cache()
def get_settings():
    settings = Settings()
    print(f"Loading Settings for: {settings.env_name}")
    return settings

