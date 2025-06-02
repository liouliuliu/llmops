import os

import dotenv
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from injector import Injector

from config.config import Config
from internal.router import Router
from internal.server import Http
from .module import ExtensionModule

# Load environment variables
loaded = load_dotenv()
conf = Config()

injector = Injector([ExtensionModule])

app = Http(__name__, conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
