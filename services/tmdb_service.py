import requests

class TmdbService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"
        self.genres = self.carregar_generos()

    def carregar_generos(self):
        url = f"{self.base_url}/genre/movie/list"
        params = {
            "api_key": self.api_key,
            "language": "pt-BR"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            generos = response.json().get("genres", [])
            return {g["id"]: g["name"] for g in generos}
        else:
            print("Erro ao carregar gêneros:", response.text)
            return {}

    def buscar_filme_por_titulo(self, titulo):
        url = f"{self.base_url}/search/movie"
        params = {
            "api_key": self.api_key,
            "query": titulo,
            "language": "pt-BR"
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("results", [])
        else:
            print(f"Erro {response.status_code}: {response.text}")
            return []

    def obter_nomes_dos_generos(self, genre_ids):
        return [self.genres.get(gid, "Desconhecido") for gid in genre_ids]