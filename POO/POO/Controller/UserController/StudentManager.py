from Model.User.Student import Student

class StudentManager:
    """Gerencia funcionalidades específicas dos estudantes."""

    def __init__(self, user_manager):
        self.user_manager = user_manager

    def filter_students(self, course):
        """Filtra e exibe todos os estudantes de um determinado curso."""
        students = [user for user in self.user_manager._user_list if isinstance(user, Student) and user.course == course]
        if students:
            for student in students:
                print(student)
        else:
            print("No students found")

    def get_progress(self, username):
        """Obtém o progresso de um estudante específico."""
        student = next((user for user in self.user_manager._user_list if isinstance(user, Student) and user.username == username), None)
        if student:
            print(f"Current progress: {student.progress}%")

    def update_progress(self, username, new_progress):
        """Atualiza o progresso de um estudante."""
        student = next((user for user in self.user_manager._user_list if isinstance(user, Student) and user.username == username), None)
        if student:
            student.progress = new_progress

    def get_course(self, username):
        """Retorna o curso de um estudante específico."""
        student = next((user for user in self.user_manager._user_list if isinstance(user, Student) and user.username == username), None)
        return student.course if student else None