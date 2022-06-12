from khl import Message, MessageTypes

from bot.api import getConfig, pluginsManager, log
from bot.api.ABot import aBot
from bot.api.ACommandManager import HELP

pluginsManager = pluginsManager.pluginsManager()
token = getConfig.getConfig("settings", "token")
help = []

bot = aBot(token=token)


def entry_point():
    pluginsManager.runPlugins()
    help_list = ""
    desc_list = ""
    for name in HELP.keys():
        help_list += f"\n`{HELP[name][0]}`"
        desc_list += f"\n{HELP[name][1]}"
    help_card = [
        {
            "type": "card",
            "theme": "secondary",
            "size": "lg",
            "modules": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain-text",
                        "content": "命令帮助"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "paragraph",
                        "cols": 2,
                        "fields": [
                            {
                                "type": "kmarkdown",
                                "content": f"**使用**{help_list}"
                            },
                            {
                                "type": "kmarkdown",
                                "content": f"**说明**{desc_list}"
                            }
                        ]
                    }
                }
            ]
        }
    ]

    @bot.command(name='help', help="/help", desc="显示帮助")
    async def help_command(msg: Message):
        await msg.reply(help_card, type=MessageTypes.CARD)

    log.logger.info("机器人已启动")
    bot.run()


def stopPlugins():
    pluginsManager.stopPlugins()
