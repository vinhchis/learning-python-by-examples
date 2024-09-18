from services.user_service import UserService
from models.user import User


def main():
    user_service = UserService()
    while True:
        print('Welcome to Manager Users System')
        print('1. View all users')
        print('2. Add a user')
        print('3. Edit a user by id')
        print('4. Delete a user by id')
        print('5. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            users = user_service.get_users()
            if users:
                print('list of users:')
                for user in users:
                    print('\t', User(*user))
            else:
                print('No users')

        if choice == '2':
            name = input('Enter your name: ')
            email = input('Enter your email: ')
            new_user_id = user_service.create_user(name, email)
            print(f"Created user with ID: {new_user_id}")

        if choice == '3':
            id = int(input('Enter your id: '))
            if user_service.get_user(id):
                print('User exists')
                new_user_name = input('Enter your new name: ')
                new_user_email = input('Enter your new email: ')

                user_service.update_user(id, new_user_name, new_user_email)
                updated_user = user_service.get_user(id)
                print(f"Updated user: {updated_user}")
            else:
                print(f'User with id={id} does not exist')

        if choice == '4':
            id = int(input('Enter your id: '))
            if user_service.get_user(id):
                user_service.delete_user(id)
                print("User deleted")
            else:
                print(f'User with id={id} does not exist')

        if choice == '5':
            break

        is_continue = input('Enter "y" to continue: ')
        if is_continue == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    main()
