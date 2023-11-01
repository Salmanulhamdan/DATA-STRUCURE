# def decrator():
#     global string
#     string="HELLO WORLD"
# decrator()
# print(string)

def hello_world_decorator(func):
    def wrapper():
        return "HELLO WORLD"

    return wrapper


@hello_world_decorator
def my_func():
    pass


result = my_func()
print(result)
