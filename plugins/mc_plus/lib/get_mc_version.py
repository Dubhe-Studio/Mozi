import json
import requests


async def get():
    x = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
    y = json.loads(x.text)['latest']
    z = "最新正式版：" + y['release'] + "\n最新快照版：" + y['snapshot']
    return z
