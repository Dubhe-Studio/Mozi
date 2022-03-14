import requests


def get(name: str):
    x = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}').json()['id']
    x = x[:8] + '-' + x[8:12] + '-' + x[12:16] + '-' + x[16:]
    return x
