from flask_sqlalchemy import SQLAlchemy
from injector import Module, Binder
from internal.extension.database_extenstion import db


class ExtensionModule(Module):
    """扩展模块的依赖注入"""
    def configure(self, binder:Binder) -> None:
        binder.bind(SQLAlchemy, to=db)