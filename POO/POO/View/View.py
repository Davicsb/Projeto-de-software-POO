from abc import ABC, abstractmethod
from colorama import init
from .shared import user_manager, course_manager

from .afterLogin.StudentView import StudentView
from .afterLogin.TeacherView import TeacherView

#from View.afterLogin.SuperUserView import SuperUserView

init(autoreset=True)



class View(ABC):
    def check_password(self, username, password):
        print(f"Checking password for {username} {password}")
        for user in user_manager.user_list:
            if user.username == username and user.password == password:
                return user
        return None

    def get_user_type(self, user):
        match user.get_role():
            case "Teacher":
                return TeacherView() 
            case "Student":
                return StudentView() 
            case "SuperUser":
                pass
                #return SuperUserView()  # Aqui deve existir a classe SuperUserView
            case _:
                return None   

    def get_username(self, user_id):
        for user in user_manager.user_list:
            if user.id == user_id:
                return user.username
        return False

