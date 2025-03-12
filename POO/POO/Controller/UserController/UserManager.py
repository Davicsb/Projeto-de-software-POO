from Model.User.Student import Student
from Model.User.Teacher import Teacher
from Model.User.SuperUser import SuperUser

class UserManager:
    """Gerencia a criação, listagem, atualização e remoção de usuários no sistema."""
    
    def __init__(self):
        self._user_list = []  
        
    def add_user(self, user):
        match user.get_role():
            case "student":
                self.add_student(user.username, user.password, user.age, user.course, user.paid)
            case  "teacher":
                self.add_teacher(user.username, user.password)
            case "superUser":
                self.add_super_user(user.username, user.password)
            case _:
                print("Invalid user!")
                
    def add_student(self, username, password, age, course, paid):
        tamanho= len(self._user_list)
        print(f"Adding student...{username, password, age, course, paid}")
        self._user_list.append(Student(username, password, age, course, paid))
        print(len(self._user_list)>tamanho)
        
    def add_teacher(self, username, password):
        tamanho= len(self._user_list)
        print(f"Adding teacher...{username, password}")
        self._user_list.append(Teacher(username, password))
        print(len(self._user_list)>tamanho)
        
    def add_super_user(self, username, password):
        print(f"Adding super user...{username, password}")
        tamanho= len(self._user_list)
        self._user_list.append(SuperUser(username, password))
        print(len(self._user_list)>tamanho)
        
    def delete_user(self, username, password):
        """Remove um usuário da lista com base no username e senha."""
        tamanho= len(self._user_list)
        self._user_list = [user for user in self._user_list if not (user.username == username and user.password == password)]
        return len(self._user_list)<tamanho
    
    def list_users(self):
        """Lista todos os usuários cadastrados."""
        for user in self._user_list:
            print(user)

    def update_account(self, user_id, username, password, new_username=None, new_password=None):
        """Atualiza informações da conta do usuário."""
        user = self.get_user(username, password)
        if user and user.id == user_id:
            user.update_account(new_username, new_password)

    def get_user(self, username, password):
        """Retorna um usuário com base no username e senha."""
        return next((user for user in self._user_list if user.username == username and user.password == password), None)
    
    def get_user_type(self, user):
        """Retorna o tipo de usuário."""
        return user.get_role()
    
    def check_password(self, username, password):
        """Verifica se a senha do usuário está correta."""
        return self.get_user(username, password)
    
    def update_progress(self, username, new_progress):
        """Atualiza o progresso de um aluno."""
        for user in self._user_list:
            if user.username == username and user.get_role()=="Student":
                    user._progress = new_progress
                    print("Progress updated!")
                    break
        else:
            print("User is not a student!")

    def get_progress(self, username):
        """Retorna o progresso de um aluno."""
        for user in self._user_list:
            if user.username == username and user.get_role()== "Student":
                    print(f"{user._progress}%")
                    break
        else:
            print("User is not a student!")
    
    def get_id(self, user):
        """Retorna o id."""
        return user._id

    def get_user_by_id(self, user_id):
        """Retorna um usuário com base no id."""
        return next((user for user in self._user_list if user._id == user_id), None)
    
    def get_course(self, id):
        for student in self._user_list:  
            if student._id == id:
                return student.course
            else:
                print("Student not found!")
                
    def filter_students(self, course):
        for student in self._user_list:
            if self.get_user_type(student) == "Student":
                if student._course == course:
                    print(f'{student}')
            else:
                print("No students found")
        