import requests
import json


def get():
    global z
    x = requests.get("https://api.oick.cn/lishi/api.php")
    y = json.loads(x.text)
    for i in range(len(y['result'])):
        if i == 0:
            z = y['result'][0]['date'] + "\t" + y['result'][0]['title']
        else:
            z = z + "\n" + y['result'][i]['date'] + "\t" + y['result'][i]['title']
    return z
