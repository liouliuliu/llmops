from dotenv import load_dotenv
from flask_migrate import Migrate
from injector import Injector

from config.config import Config
from internal.router import Router
from internal.server import Http
from pkg.sqlalchemy import SQLAlchemy
from .module import ExtensionModule

# Load environment variables
loaded = load_dotenv()
conf = Config()

injector = Injector([ExtensionModule])

app = Http(__name__,
           conf=conf,
           db=injector.get(SQLAlchemy),
           migrate=injector.get(Migrate),
           router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
