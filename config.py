from dotenv import load_dotenv
from os import environ

load_dotenv()

SECRET_KEY = environ.get('SECRET_KEY')
DATABASE_URI = environ.get('DATABASE_URI')
