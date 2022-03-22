from email import message


message = "a"


def greet(name):
    # global message   -> if we use this line it will modify global message variable
    message = "b"


greet("Borshon")
print(message)  # a
