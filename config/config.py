import  os;
from typing import Any;
from .default_config import  DEFAULT_CONFIG

def _get_env(key: str):
    """ 如果找不到，则返回默认值 """
    return os.getenv(key, DEFAULT_CONFIG.get(key))

def _get_env_bool(key: str):
    """ 如果找不到，则返回默认值 """
    value:str = _get_env()
    return value.lower() == "true" if value is not None else False

class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = False;

        # 保留数据库配置.
        self.SQLAICHEMY_DATABASE_URL = _get_env("SQLAICHEMY_DATABASE_URL")
        self.SQLAICHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLAICHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLAICHEMY_POOL_RECYCLE"))
        }
        self.SQLAICHEMY_ECHO = _get_env_bool("SQLAICHEMY_ECHO")