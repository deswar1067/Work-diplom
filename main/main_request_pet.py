import requests


def new_pets(url):
    response = requests.post(url, json={
        "id": 940,
        "name": "golden-fish",
        "status": "available"
    })
    return response


def find_pets_id(url):
    response = requests.get(url)
    return response


def update_name_pet(url, name=" "):
    response = requests.post(url, data={"name": name})
    return response


def update_name(url):
    response = requests.get(url)
    return response
