from Model.User.User import User

class Teacher(User):
    def get_role(self):
        return "Teacher"