from bot.api import log
from plugins.CivilizationSimulation.lib.getUUID import get
from bot.cli.cli_entry import bot, help
from khl import Message


def onStart():
    help.append("=======================================")
    help.append("/uuid <mcid>\t查询MCID对应的正版UUID")
    help.append("/khl \t查询自己的开黑啦ID")

    @bot.command(name='uuid')
    async def uuid_command(msg: Message, name: str):
        await msg.reply(get(name))

    @bot.command(name='khl')
    async def khl_command(msg: Message):
        await msg.reply(msg.author.username+'#'+msg.author.identify_num)

    log.INFO("插件已载入", "CivilizationSimulation")
