from colorama import Fore
from View.loginInProcessing.RegisterView import RegisterView
from .BaseView import View
from .shared import user_manager, course_manager
from .afterLogin.StudentView import StudentView
from .afterLogin.TeacherView import TeacherView
from .afterLogin.SuperUserView import SuperUserView
import os
from getpass import getpass

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    
"""Adição de dados padrão"""
course_manager.add_course("Java", "Davi", 100, True)
course_manager.add_course("Python", "Davi", 100, False)
user_manager.add_student("Davi", "estudante", "00", "Java", True)
user_manager.add_student("Mariana", "1234", "00", "Python", False)
user_manager.update_progress("Mariana", "100")
user_manager.add_teacher("Davi", "professor")
user_manager.add_super_user("adm", "adm")
clear_terminal()

# Mapeia os tipos de usuário para as classes correspondentes
USER_TYPE_MAPPING = {
    "Student": StudentView(),
    "Teacher": TeacherView(),
    "SuperUser": SuperUserView(),
}

class FirstView(View):
    def EnterView(self):
        print(Fore.CYAN + "Welcome to E-Learning Platform login!")
        username = input(Fore.YELLOW + "Enter your name: ")
        password = getpass(Fore.YELLOW + "Enter your password: ")
        user = user_manager.check_password(username, password)
        print(user)
        if user:
            user_type = user_manager.get_user_type(user)
            print(Fore.GREEN + f"{user_type}")            
            if user_type:
                USER_TYPE_MAPPING.get(user_type).view(user_manager.get_id(user))
            else:
                print(Fore.RED + "Invalid Id!")
                self.view()
        else:
            choice = input(Fore.RED + "Incorrect password!\n1 - Try again.\n2 - Back\n>>> ")
            match choice:
                case "1":
                    self.EnterView() 
                case "2":
                    self.view()  
                case _:
                    print(Fore.RED + "Invalid option! Please try again\n")
                    self.EnterView()  

    def view(self):
        while True:
            print(Fore.CYAN + "Welcome to E-Learning Platform!\nWhat do you want to do?")
            choice = input(Fore.RED + "0 - To force Stop the system\n" + Fore.YELLOW + "1 - Enter.\n2 - Register.\n>>> ")
            match choice:
                case "1":
                    self.EnterView() 
                    break
                case "2":
                    RegisterView().view() 
                    break
                case "0":
                    exit()
                case _:
                    print(Fore.RED + "Invalid option! Please try again\n")