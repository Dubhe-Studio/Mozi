from bot.api import log
from bot.api.pluginConfig import getConfig
from bot.cli.cli_entry import bot
from khl import Message

pluginName = "DevTools"


def onStart():
    admin_id = getConfig(pluginName, 'admin', 'admin', 'admin_id')

    def is_op(msg: Message) -> bool:
        return msg.author.id == admin_id

    @bot.command(name='guildid', help='/guildid', desc='查询当前服务器ID')
    async def guildid(msg: Message):
        if is_op(msg):
            await msg.reply(msg.ctx.guild.id)
        else:
            await msg.reply("您配吗？")

    @bot.command(name='channelid', help='/channelid', desc='查询当前频道ID')
    async def channelid(msg: Message):
        if is_op(msg):
            await msg.reply(msg.ctx.channel.id)
        else:
            await msg.reply("您配吗？")

    log.info(pluginName, "插件已载入")
