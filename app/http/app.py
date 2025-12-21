from injector import Injector, Binder
from internal.server.http import Http
from internal.extension.database_extenstion import db
from internal.router import Router
import dotenv;
from config.config import Config;
from injector import Module
from flask_sqlalchemy import SQLAlchemy


# 将 env 加载到环境变量当中.
dotenv.load_dotenv()
config = Config()

class ExtensionModule(Module):
    def configure(self, binder:Binder) -> None:
        binder.bind(SQLAlchemy, to=db)

injector = Injector([ExtensionModule])

app = Http(__name__,conf=config, db=injector.get(SQLAlchemy),router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)