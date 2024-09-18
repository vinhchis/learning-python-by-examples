from repositories.user_repository import UserRepository
from models.user import User

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, name, email):
        user = User(None, name, email)
        return self.repository.create(user)

    def get_users(self):
        return self.repository.read_all()

    def get_user(self, user_id):
        return self.repository.read(user_id)

    def update_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.repository.update(user)

    def delete_user(self, user_id):
        self.repository.delete(user_id)