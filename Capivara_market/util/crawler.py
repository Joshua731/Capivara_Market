import requests
from model import User


# BASE_URL = "https://rickandmortyapi.com/api/character/{}"


# def get_data_from_rick_and_morty_apis(database):
    # for i in range(1, 20):
    #     response = requests.get(BASE_URL.format(i))
    #     content_json = response.json()
    #     user_json = {k: v for k, v in content_json.items() if k in dir(User)}
    #     database.session.add(User(**user_json))
    # database.session.add(User())
    # database.session.commit()
