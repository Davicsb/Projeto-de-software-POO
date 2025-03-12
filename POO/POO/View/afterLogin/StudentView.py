from colorama import Fore
from ..shared import user_manager, course_manager

from ..BaseView import View


class StudentView(View):
    def view(self, user_id):
        user = user_manager.get_user_by_id(user_id)
        
        print(Fore.GREEN + f"Welcome {user.username} to student dashboard! What you wanna do?")
        choice = input(Fore.RED + "0 - Quit.\n" + Fore.YELLOW + "1 - Update account.\n2 - View course lessons\n3 - View quizzes\n4 - Enter Forum\n5 - Emit certificate.\n>>> ")
        
        match choice:
            case "1":
                self.update_account(user_id, user.get_role())
            case "2":
                print(Fore.GREEN + "Viewing lessons for the course...")
                course_manager.view_classes(user._course)
                self.view(user_id)
            case "3":
                print(Fore.GREEN + "Viewing quizzes...")
                course_manager.view_quizzes(user._course)
                self.view(user_id)
            case "4":
                self.forum(user_id)
            case "5":
                from Controller.Utils.certificate import fill_and_generate_certificate
                username = input("Confirm your username: ")
                password = input("Confirm your password: ")
                user = user_manager.get_user(username, password)
                if user._progress == "100":
                    fill_and_generate_certificate(user)
                else:
                    print(Fore.RED + "You are not able to emit your certificate!")
                self.view(user_id)
            case "6":
                from ..FirstView import FirstView
                print(Fore.GREEN + "Goodbye!")
                FirstView().view()
            case "0":
                print(Fore.RED + "System out\n")
                exit()
            case _:
                print(Fore.RED + "Invalid option! Please try again")
                self.view(user_id)
                
    def forum(self, user_id):
            action = input("0 - Back.\n1 - View fórum.\n2 - Add comment.\n>>> ")
            user= user_manager.get_user_by_id(user_id)
            match action:
                case "0":
                    self.view(user_id)
                case "1":
                    course_manager.view_comments_in_forum(user._course)
                    self.forum(user_id)
                case  "2":
                    comment = input("Enter your comment: ")
                    course_manager.add_comment_in_forum(user._course, user.username, comment)
                    self.forum(user_id)
                case _:
                    print(Fore.RED + "Invalid option! Please try again\n")
                    self.forum(user_id)