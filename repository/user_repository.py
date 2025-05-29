import json
import os
from model.user import User

class UserRepository:
    FILE_PATH = "user.json"

    def __init__(self):
        self.__users = self.load_users()
    
    '''Recebe um usuário, 
    adiciona-o aos usuarios  
    atraves de load_users
    e salva o novo usuario 
    em save_users'''
    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError("'user' deve ser um objeto da classe 'Usuario'.")
        self.__users.append(user)
        self.save_users(self.__users)    

    '''Carrega os usuarios.
    Lê os dados do arquivo user.json, 
    converter cada entrada em 
    um objeto da classe User, e 
    retornar uma lista desses objetos''' 
    def load_users(self):
        if not os.path.exists(self.FILE_PATH):
            return []

        with open(self.FILE_PATH, "r", encoding="utf-8") as file:
            try:
                users_data = json.load(file)
                return [User.from_dict(data) for data in users_data]
            except json.JSONDecodeError:
                return []

    '''abre ou cria um arquivo json
    caso não exista e salva os dados 
    dentro do arquivo'''
    def save_users(self, users):
        users_data = []
        for user in users:
            users_data.append(user.to_dict())

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(users_data, file, ensure_ascii=False, indent=4)
        
        self.__users = users

    '''retorna a lista 'users' 
    de objetos 'Usuario' 
    convertida em dicionário'''
    def list_users(self):
        return [user.to_dict() for user in self.__users]
    
    '''retorna a lista 'users'
    de objetos 'Usuario' '''
    def list_objects_users(self):
        return [user for user in self.__users]