from colorama import Fore
from ..shared import user_manager, course_manager
from ..BaseView import View

class RegisterView(View):
    def view(self):
        print(Fore.CYAN + "Welcome to the register view!")
        username = input(Fore.YELLOW + "Enter your username: ")
        password = input(Fore.YELLOW + "Enter your password: ")
        age = input(Fore.YELLOW + "Enter your age: ")
        
        paid = input(Fore.YELLOW + "Do you want to pay for paid courses?\n1 - Yes\n2 - No\n>>>  ")
        match(paid):
            case "1":
                paid = True
            case "2":
                paid = False
            case _:
                print(Fore.RED + "Invalid option in option payment! Please try again\n")
                self.view()

        print(Fore.GREEN + "Here is the list of available courses in your plan:")
        course_manager.list_courses(paid, None)
        
        course_title = input(Fore.YELLOW + "Enter the name of the course that you want to enroll in: ")
        while course_title not in course_manager.courses:
            course_title = input(Fore.RED + "Invalid course. Please enter the course title again: ")
        course = course_manager.courses[course_title]

        user_manager.add_user(username, password, age, course, paid)
    
        print(Fore.GREEN + "Congrats! You're registered on our platform!")
        from View.FirstView import FirstView
        FirstView.EnterView()
