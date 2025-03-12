from abc import ABC, abstractmethod
import itertools

class User(ABC):
    _id_counter = itertools.count(1)

    def __init__(self, username, password):
        self._id = next(User._id_counter)
        self._username = username
        self._password = password

    def __str__(self):
        return f"{self.__class__.__name__}(ID: {self._id}, Username: {self._username},Password: {self.password})"

    @abstractmethod
    def get_role(self):
        pass

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if new_username:
            self._username = new_username
            print(f"Username atualizado para '{self._username}'!")

    @property
    def password(self):
        return self._password  # Segurança: não exibe a senha diretamente

    @password.setter
    def password(self, new_password):
        if new_password:
            self._password = new_password
            print(f"Senha de '{self._username}' foi alterada com sucesso!")

    def update_account(self, new_username=None, new_password=None):
        """Método genérico para atualização de conta, evitando repetição de código."""
        self.username = new_username
        self.password = new_password