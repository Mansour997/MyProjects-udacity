import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True


SQLALCHEMY_ECHO = True

# TODO IMPLEMENT DATABASE URL [DONE]
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/fyyur'
