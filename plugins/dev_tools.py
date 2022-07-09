from bot.api import log
from bot.api.plugin_config import get_config
from bot.cli.cli_entry import bot
from khl import Message, api

pluginName = "DevTools"


def on_start():
    admin_id = get_config(pluginName, 'admin', 'admin', 'admin_id')

    def is_op(msg: Message) -> bool:
        return msg.author.id == admin_id

    @bot.command(name='guild', help='/guild', desc='查询当前服务器')
    async def guildid(msg: Message):
        if is_op(msg):
            await msg.reply(msg.ctx.guild.id)
            channels = await bot.client.gate.exec_req(api.Channel.list(guild_id=msg.ctx.guild.id))
            for i in channels['items']:
                if i['name'] == '🎙 语音频道':
                    print(i)
        else:
            await msg.reply("您配吗？")

    @bot.command(name='channelid', help='/channelid', desc='查询当前频道ID')
    async def channelid(msg: Message):
        if is_op(msg):
            await msg.reply(msg.ctx.channel.id)
        else:
            await msg.reply("您配吗？")

    log.info(pluginName, "插件已载入")


def onStop():
    ...
