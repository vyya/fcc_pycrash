class User:
    def __init__(self, first_name, last_name, gender, age, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.user_id = user_id
        self.login_attempts = 0

    def describe_user(self):
        print(f"Here is the {self.age} years old  user {self.first_name} {self.last_name} with user id {self.user_id}")

    def greet_user(self):
        if self.gender == 'male':
            print(f"You're welcome Mr {self.first_name} {self.last_name}"
                  f" You have a {self.login_attempts} login attempts")
        else:
            print(f"You're welcome Miss {self.first_name} {self.last_name}"
                  f" You have a {self.login_attempts} login attempts")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attemps(self):
        self.login_attempts = 0

sara = User('Sara', 'Biscuit', 'female', 23, 755)
john = User('John', 'Milligan', 'male', 42, 343)
gina = User('Gina', 'Palmer', 'female', 31, 451)
sara.increment_login_attempts()
john.increment_login_attempts()
gina.increment_login_attempts()
gina.reset_login_attemps()
sara.describe_user()
sara.greet_user()
gina.describe_user()
gina.greet_user()
john.greet_user()
john.describe_user()
