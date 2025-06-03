from services.user_service import UserService
from services.tmdb_service import TmdbService
from view.app_view import AppView

class LoginController:
    def __init__(self, user_service: UserService, tmdb_service: TmdbService):
        self.user_service = user_service
        self.tmdb_service = tmdb_service
        self.view = AppView(self)

    def verificar_login(self, usuario, senha):
        if self.user_service.validate_login(usuario, senha):
            self.view.trocar_para_pesquisa()
        else:
            return ("Usuário ou senha incorretos.\nSe é sua primeira vez aqui, experimente se cadastrar.")
        
    def cadastrar_user(self, usuario, senha):
        if self.user_service.create_user(usuario, senha):
            return ("Cadastro realizado com sucesso!\n Pressione 'login' para entrar.")
        else:
            return ("Usuário já cadastrado.\nSe já possui um cadastro, experimente logar.")

    def buscar_filme(self, titulo):
        resultados = self.tmdb_service.buscar_filme_por_titulo(titulo)
        if not resultados:
            return "Nenhum filme encontrado."
        
        texto = ""
        for filme in resultados[:5]: 
            nome = filme.get("title", "Sem título")
            data = filme.get("release_date", "Sem data")
            ids_generos = filme.get("genre_ids", [])
            nomes_generos = self.tmdb_service.obter_nomes_dos_generos(ids_generos)
            genero = ", ".join(nomes_generos) if nomes_generos else "Sem gênero"

            texto += f"{nome} ({data})\nGêneros: {genero}\n\n"
        return texto

    def iniciar_aplicacao(self):
        self.view.start()
