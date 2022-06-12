from khl import Message, MessageTypes
from khl.card import Card, Module, Types, Element, Struct, CardMessage

from bot.api import getConfig, pluginsManager, log
from bot.api.ABot import aBot
from bot.api.ACommandManager import HELP

pluginsManager = pluginsManager.pluginsManager()
token = getConfig.getConfig("settings", "token")
_help = []

bot = aBot(token=token)


def entry_point():
    pluginsManager.runPlugins()

    help_card = Card(Module.Header(text="命令帮助"), Module.Divider(), Module.Section(
        Struct.Paragraph(2,
                         Element.Text(f'**使用**', Types.Text.KMD),
                         Element.Text(f'**说明**', Types.Text.KMD)
                         )))
    for name in HELP.keys():
        help_card.append(Module.Section(
            Struct.Paragraph(2,
                             Element.Text(f'`{HELP[name][0]}`', Types.Text.KMD),
                             Element.Text(HELP[name][1], Types.Text.KMD)
                             )))
    help_card = CardMessage(help_card)

    @bot.command(name='help', help="/help", desc="显示帮助")
    async def help_command(msg: Message):
        await msg.reply(help_card, type=MessageTypes.CARD)

    log.logger.info("机器人已启动")
    bot.run()


def stopPlugins():
    pluginsManager.stopPlugins()
