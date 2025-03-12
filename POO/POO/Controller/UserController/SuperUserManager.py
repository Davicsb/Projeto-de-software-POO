from Model.User.SuperUser import SuperUser

class SuperUserManager:
    """Gerencia funcionalidades específicas dos super usuários."""

    def __init__(self, user_manager):
        self.user_manager = user_manager 

    def list_super_users(self):
        """Lista todos os super usuários cadastrados."""
        super_users = [user for user in self.user_manager._user_list if isinstance(user, SuperUser)]
        if super_users:
            for super_user in super_users:
                print(super_user)
        else:
            print("No super users found")

    def grant_permissions(self, username, permission):
        """Concede permissões específicas para um super usuário."""
        super_user = next((user for user in self.user_manager._user_list if isinstance(user, SuperUser) and user.username == username), None)
        if super_user:
            super_user.permissions.append(permission)