import requests

URL = "https://jsonplaceholder.typicode.com/users"

database = {
    1: "bob",
    2: "sven",
    3: "alice"
}


def get_user_by_id(user_id):
    return database.get(user_id)


def get_users():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    raise requests.HTTPError
