from enum import Enum

class HttpCode(str, Enum):
    """
    HTTP   基础业务代码状态
    """
    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    VALIDATE_ERROR = "validate_error"