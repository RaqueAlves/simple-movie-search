from repository.user_repository import UserRepository
from services.user_service import UserService
from services.tmdb_service import TmdbService
from controller.login_controller import LoginController

if __name__ == "__main__":
    api_key = "36c48012e7b1647612e862294e32fa21"
    repository = UserRepository()
    user_service = UserService(repository)
    tmdb_service = TmdbService(api_key)
    controller = LoginController(user_service, tmdb_service)
    controller.iniciar_aplicacao()
