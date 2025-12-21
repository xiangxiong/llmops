from pkg.response.response import Response, HttpCode, json
from internal.exception.exception import FailException, CustomException

# Test the full error handling flow that was failing
try:
    # Simulate what happens in the handle_error function
    error = FailException("测试异常")
    
    # This is what was happening in http.py line 21
    response = Response(
        code=error.code,
        message=error.message,
        data=error.data if error.data is not None else {}
    )
    
    # Test the json function as well
    json_response = json(response)
    print("Success: Full error handling flow works correctly")
    print(f"Response: {response}")
    print(f"JSON Response: {json_response}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()