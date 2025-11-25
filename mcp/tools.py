from google.adk.tools import FunctionTool

def add(a: int, b: int) -> int:
    """Returns the sum of two integers.
    
    Args:
        a: The first integer.
        b: The second integer.
    Returns:
        The sum of a and b.
    """
    return a + b

add_tool = FunctionTool(func=add)