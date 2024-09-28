def authenticate(func):
    def wrapper(*args, **kwargs):
        if is_authenticated():
            return func(*args, **kwargs)
        else:
            return "Access denied"
    return wrapper

@authenticate
def view_sensitive_data():
    return "Sensitive data"

def is_authenticated():
    return True # TODO:Replace with actual authentication logic

result = view_sensitive_data()
print(result)   