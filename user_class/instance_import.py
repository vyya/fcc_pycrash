from user import User, Privileges

heath = User('Rob', 'Heath', 'male', '28', 1285)
heath.describe_user()
heath_adm = Privileges()
heath_adm.show_privileges()