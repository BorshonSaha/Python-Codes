# two types of function:
# 1 -> perform a task
# 2 -> return a value
# In python by default a function return a none value if there is no return statement

def greet(name):
    print(f"Hi {name}")


def get_greet(name):
    return f"Hi {name}"


message = get_greet("Borshon")
print(message)
# file = open("content.txt", "w")
# file.write(message)
