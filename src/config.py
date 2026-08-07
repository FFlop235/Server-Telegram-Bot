import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    PROXY_URL: str = os.getenv("PROXY_URL", "")
    ADMIN_ID: int = int(os.getenv("ADMIN_ID", 0))

settings = Settings()