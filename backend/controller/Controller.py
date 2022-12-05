from models.Person import Person
from routes.RequestApi import RequestApi

import json

class Controller:

    @staticmethod
    def get_information(id : int):
        print(id)
        results = RequestApi.get_information(id)
        print(results)

    @staticmethod
    def get_image_path(poster_path):
        return f"https://image.tmdb.org/t/p/w185{poster_path}"

    @staticmethod
    def get_person(person : str):
        results = RequestApi.get_id_person(person)
        person_information = RequestApi.get_information_person(results)
        person = Person(
            person_information['id'],
            person_information['name'],
            person_information['birthday'],
            person_information['deathday'],
            person_information['place_of_birth'],
            person_information['popularity'],
            person_information['gender'],
            person_information['known_for_department'],
            Controller.get_image_path(person_information['profile_path']),
            person_information['biography'],
            person_information['homepage']
        )
        return person