import json
import os
from . import pro_dir


def readJson(name, file="config", key="settings"):
    json_dir = os.path.join(pro_dir, 'configs', name)
    json_file = os.path.join(json_dir, file + ".json")
    if not os.path.isdir(os.path.join(pro_dir, 'configs')):
        os.mkdir(os.path.join(pro_dir, 'configs'))
    if not os.path.isdir(json_dir):
        os.mkdir(json_dir)
    if not os.path.isfile(json_file):
        file = open(json_file, 'w+', encoding='utf-8')
        json.dump({}, file, ensure_ascii=False)
        file.close()

    json_file_wr = open(json_file, 'r+', encoding='utf-8')
    json_read = json.loads(json_file_wr.read())
    try:
        return json_read[key]
    except:
        json_read[key] = []
        json_file_w = open(json_file, 'w+', encoding='utf-8')
        json.dump(json_read, json_file_w, ensure_ascii=False)
        return []


def writeJson(name, file="config", key="settings", value: list = None):
    json_dir = os.path.join(pro_dir, 'configs', name)
    json_file = os.path.join(json_dir, file + ".json")
    if not os.path.isdir(os.path.join(pro_dir, 'configs')):
        os.mkdir(os.path.join(pro_dir, 'configs'))
    if not os.path.isdir(json_dir):
        os.mkdir(json_dir)
    if not os.path.isfile(json_file):
        file = open(json_file, 'w+', encoding='utf-8')
        json.dump({}, file, ensure_ascii=False)
        file.close()

    json_file_wr = open(json_file, 'r+', encoding='utf-8')
    json_read = json.loads(json_file_wr.read())
    try:
        if value not in json_read[key]:
            json_read[key] = value
            json_file_w = open(json_file, 'w+', encoding='utf-8')
            json.dump(json_read, json_file_w, ensure_ascii=False)
        return 'OK'
    except:
        return 'ERROR'
