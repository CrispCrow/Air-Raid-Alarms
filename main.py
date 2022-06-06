from dotenv import load_dotenv
load_dotenv()

from src.app import app
from src.config import config

if __name__ == '__main__':
    app.run(**config['run_settings'])
