import requests


def new_pets(url):
    response = requests.post(url, json={
        "id": 938,
        "category": {
            "id": 22,
            "name": "fish"
        },
        "name": "golden-fish",
        "photoUrls": [
            "None"
        ],
        "tags": [
            {
                "id": 1113,
                "name": "fish-tags"
            }
        ],
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
