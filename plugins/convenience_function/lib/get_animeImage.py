import requests
from bot.api.reply_lmage import MessageImage


def get(image_type="pc"):
    x = requests.get("https://api.oick.cn/random/api.php?type="+image_type)
    y = MessageImage(x.url)
    return y
