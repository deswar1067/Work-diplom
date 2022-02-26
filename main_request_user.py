import requests


def create_user(url):

    response = requests.post(url, json={
            "id": 2,
            "username": "deswar1067",
            "firstName": "dima",
            "lastName": "gavr",
            "email": "deswar1067@tu.by",
            "password": "123",
            "phone": "+375336885425",
            "userStatus": 1111})
    return response


def register_user(url, user_name, password):
    response = requests.get(url, json={'username': user_name, 'password': password})
    return response


def get_data_user(url, user_name=" "):
    response = requests.get(url, json={"username": user_name})
    return response


def logout(url):
    response = requests.get(url)
    return response


def delete_user(url):
    response = requests.delete(url)
    return response
