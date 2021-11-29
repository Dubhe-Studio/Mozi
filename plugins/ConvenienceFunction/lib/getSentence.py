import requests


def get():
    x = requests.get("http://api.guaqb.cn/v1/onesaid/")
    return x.text

