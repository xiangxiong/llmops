import  os;
from typing import Any;
from .default_config import  DEFAULT_CONFIG

def _get_env(key: str):
    """ 如果找不到，则返回默认值 """
    return os.getenv(key, DEFAULT_CONFIG.get(key))

def _get_env_bool(key: str):
    """ 如果找不到，则返回默认值 """
    value:str = _get_env(key)
    return value.lower() == "true" if value is not None else False

class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = False;

        # 保留数据库配置.
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLAICHEMY_DATABASE_URL")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLAICHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLAICHEMY_POOL_RECYCLE"))
        }
        self.SQLALCHEMY_ECHO = _get_env_bool("SQLAICHEMY_ECHO")