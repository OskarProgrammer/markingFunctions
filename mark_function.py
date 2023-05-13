
def mark(func):
    """
    Function that marks the function as name of that function

    params: func -> any function that you want to start
    
    returns: wrapper -> function that show the name of the function that had been called
    """
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__} started")

        func(*args, **kwargs)

        print(f"Function: {func.__name__} finished working")
    return wrapper

# @mark
# def test():
#     print("hello")

# test()

