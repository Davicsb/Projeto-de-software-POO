from colorama import Fore, Style
from getpass import getpass

from ..shared import user_manager, course_manager, clear_terminal
from ..BaseView import View

class SuperUserView(View):
    def view(self, user_id):
        user = user_manager.get_user_by_id(user_id)

        print(Fore.GREEN + f"Welcome {user.username} to super user view! What you wanna do?")
        choice = input(Fore.RED + "0 - To force Stop the system\n" + Fore.YELLOW + "1 - Manage users.\n2 - Manage courses.\n3 - Quit.\n>>> ")
        match choice:
            case "0":
                print(Fore.RED + "System out\n")
                exit()
                
            case "1":
                self.manage_users(user_id)

            case "2":
                self.manage_courses(user_id)
                
            case "3":
                from ..FirstView import FirstView
                print(Fore.GREEN + "Goodbye\n")
                FirstView().view()
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.view(user_id)

    def update_user(self, user_id):
        password = getpass(Fore.YELLOW + "Enter your current password: ")
        super().update_user(user_id, password)
        self.view(user_id)
        
    def manage_users(self, user_id):
        print(Fore.GREEN + "Managing users...")
        action = input(Fore.YELLOW + "0 - Back.\n1 - List users.\n2 - Delete a user.\n>>> ")
        match action:
            case "0":
                clear_terminal()
                self.view(user_id)
            
            case "1":
                clear_terminal()
                user_manager.list_users()
                self.manage_users(user_id)
                
            case "2":
                clear_terminal()
                username = input(Fore.YELLOW + "Please confirm the usename: ")
                password = getpass(Fore.YELLOW + "Please confirm the password: ")
                                
                if user_manager.delete_user(username, password):
                    print(Fore.YELLOW + "{username} has been deleted!")
                    
                else:
                    clear_terminal()
                    choice = input(Fore.RED + "Incorrect password!\n0 - to force Stop the System\n" + Fore.YELLOW + "1 - Try again.\n2 - Back\n>>> " + Style.RESET_ALL)
                    match choice:
                        case "0":
                            print(Fore.RED + "System out\n")
                            exit()
                        case "1":
                            self.manage_users()
                        case "2":
                            self.view(user_id)
                self.view(user_id)
                
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.manage_users(user_id) 
        
    def manage_courses(self, user_id):
        print(Fore.GREEN + "Managing courses...")
        action = input(Fore.YELLOW + "0 - Back.\n1 - Create a course.\n2 - Update a couse.\n3 - Delete a course.\n4 - List courses\n5 - List leassons\n>>> ")
        match action:
            case "0":
                clear_terminal()
                self.view(user_id)
                
            case "1":
                clear_terminal()
                title = input("Enter the course title: ")
                teacher = input("Enter the teacher's name: ")
                hours = input("Enter the course hours: ")
                amount_of_classes = int(input("How many classes this course have? "))
                paid = bool(input("This course has only paid access? (True or False) "))
                course_manager.add_course(title, teacher, hours, paid)
                for current in range(amount_of_classes):
                    title_of_class = input(f"Enter the title of the {current + 1}º class: ")
                    url = input(f"Enter the url of the {current + 1}º class: ")
                    course_manager.add_class(title, title_of_class, url)
                self.manage_courses(user_id)
                    
            case "2":
                clear_terminal()
                old_title = input("Enter the course title to update: ")
                new_title = input("Enter the new title (leave empty to keep current): ") or None
                new_hours = input("Enter the new hours (leave empty to keep current): ") or None
                new_teacher = input("Enter the new teacher (leave empty to keep current): ") or None
                course_manager.update_course(old_title, new_title, new_hours, new_teacher)
                self.manage_courses(user_id)
                
            case "3":
                clear_terminal()
                title = input("Enter the course title to delete: ")
                course_manager.delete_course(title)
                self.manage_courses(user_id)
                
            case "4":
                clear_terminal()
                course_manager.list_courses(True, None)
                self.manage_courses(user_id)
            
            case "5":
                clear_terminal()
                title = input("Enter the course title: ")
                course_manager.view_classes(title)
                self.manage_courses(user_id)
                
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.manage_courses(user_id)    
