from pkg.sqlalchemy import SQLAlchemy
from injector import Module, Binder
from internal.extension.database_extenstion import db
from internal.extension.migrate_extension import migrate


class ExtensionModule(Module):
    """扩展模块的依赖注入"""
    def configure(self, binder:Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        # binder.bind(Migrate, to=migrate)