from rcon import Client
from bot.api.plugin_config import get_config
from khl.card import CardMessage, Card, Module, Struct, Element, Types


def __runcommand(command: str, parameter: str = None):
    address = get_config('MCPlus', 'config', 'rcon', 'address')
    port = int(get_config('MCPlus', 'config', 'rcon', 'port'))
    password = get_config('MCPlus', 'config', 'rcon', 'password')
    with Client(address, port, passwd=password) as client:
        response = client.run(command, parameter)
        return response


def whitelist_add(name: str):
    get = __runcommand('whitelist', 'add ' + name)
    return get


def seed():
    get = __runcommand('execute', 'run seed')
    return get


def time():
    get1 = __runcommand('execute', 'run time query daytime').replace('The time is ', '')
    get2 = __runcommand('execute', 'run time query day').replace('The time is ', '')
    get3 = __runcommand('execute', 'run time query gametime').replace('The time is ', '')
    get = CardMessage(Card(Module.Section(Struct.Paragraph(2, Element.Text('**daytime**', Types.Text.KMD), Element.Text(f'`{get1}`', Types.Text.KMD))),
                           Module.Section(Struct.Paragraph(2, Element.Text('**day**', Types.Text.KMD), Element.Text(f'`{get2}`', Types.Text.KMD))),
                           Module.Section(Struct.Paragraph(2, Element.Text('**gametime**', Types.Text.KMD), Element.Text(f'`{get3}`', Types.Text.KMD)))))
    return get
