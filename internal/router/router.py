from crypt import methods

from flask import Flask,Blueprint
from llmops.internal.handler.app_handler import AppHandler
from injector import inject
from dataclasses import dataclass

@inject
@dataclass
class Router:
    # 路由
    app_handler: AppHandler
    """ 路由类 """
    # def __init__(self,app_handler: AppHandler):
    #     self.app_handler = app_handler

    def register_route(self,app:Flask):
        # 1、创建蓝图
        bp = Blueprint('llmops',__name__,url_prefix="")

        # 2、注册路由
        bp.add_url_rule('/ping',view_func=self.app_handler.ping)
        bp.add_url_rule('/completion',methods=['POST'],view_func=self.app_handler.completion)

        # 在应用上注册蓝图
        app.register_blueprint(bp)

# r = Router(AppHandler())