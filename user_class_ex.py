class User:
    def __init__(self, first_name, last_name, gender, age, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.user_id = user_id

    def describe_user(self):
        print(f"Here is the {self.age} years old  user {self.first_name} {self.last_name} with user id {self.user_id}")

    def greet_user(self):
        if self.gender == 'male':
            print(f"You're welcome Mr {self.first_name} {self.last_name}")
        else:
            print(f"You're welcome Miss {self.first_name} {self.last_name}")

sara = User('Sara', 'Biscuit', 'female', 23, 755)
john = User('John', 'Milligan', 'male', 42, 343)
gina = User('Gina', 'Palmer', 'female', 31, 451)
sara.describe_user()
sara.greet_user()
gina.describe_user()
gina.greet_user()
john.greet_user()
john.describe_user()
