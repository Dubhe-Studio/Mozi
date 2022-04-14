import json
import os
from . import pro_dir


def readJson(plugin: str = "settings", file: str = "config", key: any = None) -> any:
    configs_dir = os.path.join(pro_dir, 'configs')
    if not os.path.isdir(configs_dir):
        os.mkdir(configs_dir)
    json_dir = os.path.join(configs_dir, plugin)
    if not os.path.isdir(json_dir):
        os.mkdir(json_dir)
    json_file = os.path.join(json_dir, file) + '.json'
    if not os.path.isfile(json_file):
        with open(json_file, 'w') as jsonStr:
            jsonStr.write('{}')
            jsonStr.close()
    jsonStr = open(json_file, 'r', encoding='utf8').read()
    jsonStr = json.loads(jsonStr)
    return jsonStr[key]


def writeJson(plugin: str = "settings", file: str = "config",  key: any = None, value: any = None) -> bool:
    configs_dir = os.path.join(pro_dir, 'configs')
    if not os.path.isdir(configs_dir):
        os.mkdir(configs_dir)
    json_dir = os.path.join(configs_dir, plugin)
    if not os.path.isdir(json_dir):
        os.mkdir(json_dir)
    json_file = os.path.join(json_dir, file) + '.json'
    if not os.path.isfile(json_file):
        with open(json_file, 'w') as jsonStr:
            jsonStr.write('{}')
            jsonStr.close()
    jsonStr = open(json_file, 'r', encoding='utf8').read()
    jsonStr = json.loads(jsonStr)
    jsonStr[key] = value
    try:
        jsonStr = json.dumps(jsonStr, ensure_ascii=False, indent=4)
        open(json_file, 'w', encoding='utf8').write(jsonStr)
        return True
    except:
        return False
