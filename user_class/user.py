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
