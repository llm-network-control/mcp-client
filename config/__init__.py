"""
Config package
"""
from os import getenv
from dotenv import load_dotenv

load_dotenv()

SERVER_CONNECTION_HOST = getenv('SERVER_CONNECTION_HOST', '127.0.0.1')
SERVER_PORT = int(getenv('SERVER_PORT', '9000'))
OPENROUTER_API_KEY = getenv('OPENROUTER_API_KEY')
