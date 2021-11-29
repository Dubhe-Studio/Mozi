import requests
from bot.api.replyImage import messageImage


def get(image_type="pc"):
    x = requests.get("https://api.oick.cn/random/api.php?type="+image_type)
    y = messageImage(x.url)
    return y
