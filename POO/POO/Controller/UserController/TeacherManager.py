from Model.User.Teacher import Teacher

class TeacherManager:
    """Gerencia funcionalidades específicas dos professores."""

    def __init__(self, user_manager):
        self.user_manager = user_manager 

    def list_teachers(self):
        """Lista todos os professores cadastrados."""
        teachers = [user for user in self.user_manager._user_list if isinstance(user, Teacher)]
        if teachers:
            for teacher in teachers:
                print(teacher)
        else:
            print("No teachers found")

    def assign_course(self, teacher_name, course):
        """Atribui um curso a um professor."""
        teacher = next((user for user in self.user_manager._user_list if isinstance(user, Teacher) and user.username == teacher_name), None)
        if teacher:
            teacher.course = course