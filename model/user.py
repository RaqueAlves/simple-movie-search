class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password 

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password == self.user_name:
            raise ValueError("A senha não pode ser igual ao nome de usuário.")
        self.__password = password

    def to_dict(self):
        return {
            "username": self.user_name,
            "password": self.password
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(user_name=data["username"], password=data["password"])