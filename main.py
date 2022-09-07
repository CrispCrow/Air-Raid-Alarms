from dotenv import load_dotenv
load_dotenv()

from src.app import app
from src.config import config

import waitress

if __name__ == '__main__':
    waitress.serve(app)
