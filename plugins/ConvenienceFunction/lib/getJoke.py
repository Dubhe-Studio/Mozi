import random
import requests
import json


def get():
    page = random.randint(1, 874)
    x = requests.get("https://api.apiopen.top/getJoke?page="+str(page)+"&count=1&type=text")
    return json.loads(x.text)['result'][0]['text']
