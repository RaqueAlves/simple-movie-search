from model.user import User
from repository.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    '''Cria um usuario.
    Tenta encontrar o usuario pelo nome,
    caso já exista, retorna false,
    caso contrário, cria um novo User,
    adiciona ao repositório e retorna true.'''
    def create_user(self, name, password):
        if self.get_user_by_name(name):
            return False
        
        new_user = User(name, password)
        self.repository.add_user(new_user)
        return True
        
    '''Valida o login.
    Verifica a lista de objetos usuario
    compara o nome e a senha. Se concidirem,
    retorna True, se não, retorna False'''
    def validate_login(self, username, password):
        users = self.repository.list_objects_users()
        for user in users:
            if user.user_name == username and user.password == password:
                return True
        return False


    '''Busca o usuario pelo nome.
    Percorre a lista de objetos usuario 
    no repositório e compara o nome dos
    objetos com o nome informado, se for igual,
    retorna o usuario, se não, retorna None.'''
    def get_user_by_name(self, name):
        users = self.repository.list_objects_users()
        for user in users:
            if user.user_name == name:
                return user
        return None

    '''Lista os usuarios.
    Retorna a lista de usuarios
    do repositório.'''
    def list_users(self):
        return self.repository.list_users()