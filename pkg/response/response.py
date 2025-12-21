from dataclasses import field,dataclass
from typing import Any
from flask import jsonify
from pkg.response.http_code import HttpCode


@dataclass
class Response:
    """
    响应类
    """
    code: HttpCode
    message: str
    data: Any = field(default_factory=dict)


def json(data:Response = None):
    """ 基础响应接口 """
    return jsonify(data),200


def success_json(data:Any = None):
    """ 成功响应接口 """
    return json(Response(code=HttpCode.SUCCESS,message="",data=data))


def fail_json(data:Any = None):
    """ 失败响应接口 """
    return json(Response(code=HttpCode.FAIL,message="",data=data))


def message(code:HttpCode = None,msg:str =""):
    """ 错误信息响应接口 """
    return json(Response(code=code,message=msg,data={}))

def success_message(msg: str = ""):
    """成功的消息响应"""
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    """失败的消息响应"""
    return message(code=HttpCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    """未找到消息响应"""
    return message(code=HttpCode.NOT_FOUND, msg=msg)

def unauthorized_message(msg: str = ""):
    """未授权消息响应"""
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)

def forbidden_message(msg: str = ""):
    """无权限消息响应"""
    return message(code=HttpCode.FORBIDDEN, msg=msg)
