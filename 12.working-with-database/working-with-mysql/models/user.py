class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f'User(id={self.id:2d}|name={self.name:15}|email={self.email:20})'