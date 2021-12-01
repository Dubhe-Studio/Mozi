from rcon import Client
from bot.api.PluginConfig import getConfig


def __runcommand(command: str, parameter: str):
    address = getConfig('MCPlus', 'config', 'rcon', 'address')
    port = int(getConfig('MCPlus', 'config', 'rcon', 'port'))
    password = getConfig('MCPlus', 'config', 'rcon', 'password')
    with Client(address, port, passwd=password) as client:
        response = client.run(command, parameter)
        return response


def whitelistAdd(name: str):
    get = __runcommand('whitelist', 'add ' + name)
    return get
