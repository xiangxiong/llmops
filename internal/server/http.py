from flask import Flask, typing as ft;

from internal.model import App
from internal.router import Router;
from config.config import Config;
from internal.exception import CustomException;
from pkg.response import json, Response, HttpCode
from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class Http(Flask):



    def __init__(self, *args,conf: Config,
                 db: SQLAlchemy, migrate: Migrate, router:
                Router, **kwargs):
        super().__init__(*args, **kwargs)

        router.register_route(self)

        self.config.from_object(conf)

        self.register_error_handler(Exception, self.handle_error)

        # 初始化扩展
        db.init_app(self)
        with self.app_context():
            _ = App()
            db.create_all()
        # migrate.init_app(self, db)


    def handle_error(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {}
            ))

        return json(Response(
            code=HttpCode.FAIL,
            message=str(error),
            data=None
        ))
        # return  error.message