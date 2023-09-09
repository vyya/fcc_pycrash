from user import User

class Privileges:

    def __init__(self, privileges = ['can add user', 'can ban user', 'can delete user']):
        self.privileges = privileges

    def show_privileges(self):
        print(f"""\nAdmin has the following privileges:""")
        for privilege in self.privileges:
            print(f'- {privilege}')

class Admin(User):
    def __init__(self, first_name, last_name, gender, age, user_id):
        super().__init__(first_name, last_name, gender, age, user_id)
        self.privileges = Privileges()