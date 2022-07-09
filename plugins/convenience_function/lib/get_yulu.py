import requests


def get():
    x = requests.get("https://api.oick.cn/yulu/api.php")
    return x.text
