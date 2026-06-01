# Define a decorator function that takes another function as input
def my_decorator(func):
    
    # Define an inner function (the wrapper) that adds extra behavior
    def wrapper():
        print("Before the function runs")   # Code that runs before the original function
        func()                              # Call the original function
        print("After the function runs")    # Code that runs after the original function
    
    # Return the wrapper function so it replaces the original
    return wrapper


# Apply the decorator to say_hello using @ syntax
@my_decorator
def say_hello():
    print("Hello!")   # The original function just prints "Hello!"


# Call the decorated function
say_hello()