from services.user_service import UserService
from view.login_view import LoginView

class LoginController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.view = LoginView(self)

    def verificar_login(self, usuario, senha):
        if self.user_service.validate_login(usuario, senha):
            self.view.mostrar_mensagem("Sucesso", "Login realizado com sucesso!")
        else:
            self.view.mostrar_mensagem("Erro", "Usuário ou senha incorretos.\nSe é sua primeira vez aqui, experimente se cadastrar.")
        
    def cadastrar_user(self, usuario, senha):
        if self.user_service.create_user(usuario, senha):
            self.view.mostrar_mensagem("Sucesso", "Cadastro realizado com sucesso!\n Pressione 'login' para entrar.")
        else:
            self.view.mostrar_mensagem("Erro", "Usuário já cadastrado.\nSe já possui um cadastro, experimente logar.")

    def iniciar_aplicacao(self):
        self.view.start()
