import requests
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def create_new_user():
    data_user = []
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(5)
    payload = {
        "email": email,
        "password": password,
        "name": name
        }
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
    if response.status_code == 200:
        data_user.append(email)
        data_user.append(password)
        data_user.append(name)
        token = response.json()['accessToken']
    return email, password, token