from pkg.response.response import Response, HttpCode

# Test creating a Response instance
try:
    response = Response(
        code=HttpCode.SUCCESS,
        message="Test message",
        data={"test": "data"}
    )
    print("Success: Response instance created successfully")
    print(f"Response: {response}")
except TypeError as e:
    print(f"Error: {e}")
    print("Failed to create Response instance")