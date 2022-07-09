from khl import Message, MessageTypes
from khl.card import Card, Module, Types, Element, Struct, CardMessage

from bot.api import get_config, plugins_manager, log
from bot.api.bot import ABot
from bot.api.command_manager import HELP

pluginsManager = plugins_manager.plugins_manager()
token = get_config.get_config("settings", "token")

bot = ABot(token=token)


def entry_point():
    pluginsManager.run_plugins()

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
        if msg.ctx.channel.id != '11521515' and msg.ctx.channel.id != 'xxxx':
            await msg.reply(help_card, type=MessageTypes.CARD)

    log.logger.info("机器人已启动")
    bot.run()


def stop_plugins():
    pluginsManager.stop_plugins()
