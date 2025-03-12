import os

from Controller import UserManager, CourseManager

# Criando instâncias dos gerenciadores
course_manager = CourseManager()  
user_manager = UserManager()  

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")