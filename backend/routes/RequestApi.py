import requests

key = 'INSIRA SUA CHAVE AQUI'

class RequestApi:
    
    @staticmethod
    def get_movie_popular_by_genre(genre: int):
        endpoint = f'https://api.themoviedb.org/3/discover/movie/?api_key={key}&certification_country=US&certification=R&sort_by=vote_count.desc&with_genres={genre}'
        r = requests.get(endpoint)
        data = r.json()
        results = data['results']
        return results

    @staticmethod
    def get_id_person(person: str):
        endpoint = f'https://api.themoviedb.org/3/search/person?api_key={key}&query={person}'
        r = (requests.get(endpoint)).json()
        result = r['results']
        for person in result:
            id = person['id']
        return id

    @staticmethod
    def get_information_person(id: int):
        endpoint = f'https://api.themoviedb.org/3/person/{id}?api_key={key}'
        r = (requests.get(endpoint)).json()
        return r




        