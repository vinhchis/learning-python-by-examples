class Authenticate:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        if self.is_authenticated():
            return self.func(*args, **kwargs)
        else:
            return "Access denied"

def is_authenticated(self):
    return True # Replace with the actual authentication logic

@Authenticate
def view_sensitive_data():
    return "Sensitive data"
    
result = view_sensitive_data()
print(result)