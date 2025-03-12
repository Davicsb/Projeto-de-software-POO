from ..shared import user_manager, course_manager
from colorama import Fore
from ..BaseView import View

class TeacherView(View):
    def view(self, user_id):
        user = user_manager.get_user_by_id(user_id)
        print(Fore.GREEN + f"Welcome {user.username} to teacher dashboard! What you wanna do?")
        choice = input(Fore.RED + "0 - To force Stop the system\n" + Fore.YELLOW + "1 - Update account.\n2 - Manage your courses.\n3 - Manage your students.\n4 - Quit\n>>> ")
        match choice:
            case "0":
                print(Fore.RED + "System out\n")
                exit()
            case "1":
                user_manager.update_user(user_id)
            case "2":
                print(Fore.GREEN + "Managing courses...")
                self.manage_courses(user_id)
            case "3":
                print(Fore.GREEN + "Viewing your students...")
                self.manage_students(user_id)
            case "4":
                from ..FirstView import FirstView
                print(Fore.GREEN + "Goodbye\n")
                FirstView().view()
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.view(user_id)

    def manage_students(self, user_id):
        action = input(Fore.YELLOW + "0 - Back.\n1 - List your students.\n2 - Track student progress.\n>>> ")
        match action:
            case "0":
                self.view(user_id)
            case "1":
                course = input("Which course do you want to filter: ")
                user_manager.filter_students(course)
                self.manage_students(user_id)
            case "2":
                self.track_progress(user_id)
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.manage_courses(user_id)

    def track_progress(self, user_id):
        action = input(Fore.YELLOW + "0 - Back.\n1 - View progress.\n2 - Update progress.\n>>> ")
        match action:
            case "0":
                self.manage_students(user_id)
            case "1":
                name = input("Enter the student's username: ")
                user_manager.get_progress(name)
                self.track_progress(user_id)
            case "2":
                name = input("Enter the student's username: ")
                new_progress = input("Enter the new progress: ")
                user_manager.update_progress(name, new_progress)
                self.track_progress(user_id)

    def manage_courses(self, user_id):
        action = input(Fore.YELLOW + "0 - Back.\n1 - List your courses.\n2 - Update your courses.\n3 - Quizzes.\n4 - Fórum\n>>> ")
        match action:
            case "0":
                self.view(user_id)
            case "1":
                course_manager.list_courses(True, user_manager.get_user_by_id(user_id).username)
                self.manage_courses(user_id)
            case "2":
                old_title = input("Enter the course title to update: ")
                new_title = input("Enter the new title (leave empty to keep current): ") or None
                new_hours = input("Enter the new hours (leave empty to keep current): ") or None
                new_teacher = input("Enter the new teacher (leave empty to keep current): ") or None
                course_manager.update_course(old_title, new_title, new_hours, new_teacher)
                self.manage_courses(user_id)
            case "3":
                self.quizzes(user_id)
            case "4":
                self.forum(user_id)
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.manage_courses(user_id)
                
    def quizzes(self, user_id):
        action = input("0 - Back.\n1 - View quizzes.\n2 - Add quizzes\n3 - Delete a quiz.\n>>> ")
        match action:
            case "0":
                self.manage_courses(user_id)
                
            case "1":
                title = input("Enter the course title: ")
                course_manager.view_quizzes(title)
                self.quizzes(user_id)
            
            case  "2":
                title = input("Enter the course title: ")
                amount_of_quizzes = int(input("How manny quizzes do you wanna add: "))
                for i in range(amount_of_quizzes):
                    quiz = input("Enter the question: ")
                    answer = input("Enter the quiz answer: ")
                    course_manager.add_quiz(title, quiz, answer)
                self.quizzes(user_id)
            
            case "3":
                title = input("Enter the course title: ")
                question = input("Enter the question that youn wanna delete: ")
                course_manager.remove_quiz(title, question)
                self.quizzes(user_id)
                
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.quizzes(user_id)
                
    def forum(self, user_id):
        action = input("0 - Back.\n1 - View fórum.\n2 - Add comment.\n3 - Delete a comment.\n>>> ")
        match action:
            case "0":
                self.manage_courses(user_id)
                
            case "1":
                title = input("Enter the course title: ")
                course_manager.view_comments_in_forum(title)
                self.forum(user_id)
            
            case  "2":
                title = input("Enter the course title: ")
                comment = input("Enter your comment: ")
                course_manager.add_comment_in_forum(title, user_manager.get_user_by_id(user_id).username, comment)
                self.forum(user_id)
            
            case "3":
                title = input("Enter the course title: ")
                username = input("Enter the username of the comment: ")
                comment = input("Enter the comment that you wanna delete: ")
                course_manager.remove_comment(title, username, comment)
                self.forum(user_id)
            
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.forum(user_id)