from injector import Injector, Binder
from app.http.module import ExtensionModule
from internal.server.http import Http
from internal.extension.database_extenstion import db
from internal.router import Router
import dotenv;
from config.config import Config;
from injector import Module
from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 将 env 加载到环境变量当中.
dotenv.load_dotenv()
config = Config()

injector = Injector([ExtensionModule])

app = Http(__name__,conf=config, db=injector.get(SQLAlchemy), migrate=injector.get(Migrate), router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)