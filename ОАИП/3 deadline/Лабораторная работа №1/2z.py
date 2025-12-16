def make_bold(func):
    def wrapper():
        result = func()
        return f"<b>{result}</b>"
    return wrapper
def get_text():
    return "Hello, World!"
print(get_text())
