from bot.api import log
from bot.api.pluginConfig import getConfig
from bot.cli.cli_entry import bot, help
from khl import Message


def onStart():
    help.append("=======================================")
    help.append("/guildid \t查询当前服务器ID")
    help.append("/channelid \t查询当前频道ID")
    admin_id = getConfig('DevTools', 'admin', 'admin', 'admin_id')

    def is_op(msg: Message) -> bool:
        return msg.author.id == admin_id

    @bot.command(name='guildid')
    async def guildid(msg: Message):
        if is_op(msg):
            await msg.reply(msg.ctx.guild.id)
        else:
            await msg.reply("您配吗？")

    @bot.command(name='channelid')
    async def channelid(msg: Message):
        if is_op(msg):
            await msg.reply(msg.ctx.channel.id)
        else:
            await msg.reply("您配吗？")

    log.info("DevTools", "插件已载入")
