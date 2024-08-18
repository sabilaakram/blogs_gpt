from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret)
# NGROK_URL = config("NGROK_URL", default="http://localhost:8000")
NGROK_URL = config( default="http://localhost:8000")
