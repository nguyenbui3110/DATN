import os
from dotenv import load_dotenv
from datetime import timedelta
load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
MODEL=os.environ.get("MODEL_PATH")