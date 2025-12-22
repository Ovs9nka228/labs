def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper
@make_bold
def greet(name):
    return f"Hello, {name}!"
print(greet("World"))
