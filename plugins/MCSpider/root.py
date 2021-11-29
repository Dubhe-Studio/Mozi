from plugins.MCSpider.lib import getMcServer, getMcVersion
from bot.cli.cli_entry import bot, help
from bot.api import log
from bot.lib import Message


def onStart():
    help.append("=======================================")
    help.append("/mcv\t查询最新的Minecraft版本")
    help.append("/server <address>\t获取某服务器的信息")

    @bot.command(name='mcv')
    async def mcv_command(msg: Message):
        await msg.reply(getMcVersion.get())

    @bot.command(name='server')
    async def server_command(msg: Message, address: str = "0"):
        await msg.reply(getMcServer.getServer(address))

    log.Log("插件已载入", "MCSpider")
