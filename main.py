from services.user_service import UserService
from repository.user_repository import UserRepository
from controller.login_controller import LoginController

if __name__ == "__main__":
    repository = UserRepository()
    service = UserService(repository)
    app = LoginController(service)
    app.iniciar_aplicacao()