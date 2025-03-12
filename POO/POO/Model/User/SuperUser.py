from Model.User.User import User 

class SuperUser(User):
    def get_role(self):
        return "SuperUser"

    @staticmethod
    def register_teacher(user_manager, teacher_username, teacher_password):
        """Evita importação interna e passa a responsabilidade para um gerenciador externo."""
        user_manager.add_teacher(teacher_username, teacher_password)

    @staticmethod
    def register_super_user(user_manager, super_user_username, super_user_password):
        user_manager.add_super_user(super_user_username, super_user_password)