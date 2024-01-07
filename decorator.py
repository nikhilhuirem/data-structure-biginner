# decorator is a function that takes another function as arguments and returns a function

def decorator(func):
    def wrapper():
        print("Payment initiated")
        func()
        print("Payment successfull")
    return wrapper

@decorator
def hello():
    print("Do all the requirements")

hello()

# or 
# return = decorator(hello)
# return()