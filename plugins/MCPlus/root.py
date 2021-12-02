from bot.api.pluginConfig import getConfig
from plugins.MCPlus.lib import getMcServer, getMcVersion, runCommand
from bot.cli.cli_entry import bot, help
from bot.api import log, pluginJson
from bot.lib import Message


def onStart():
    help.append("=======================================")
    help.append("/mcv\t查询最新的Minecraft版本")
    help.append("/server <address>\t获取某服务器的信息")

    channel_id = pluginJson.readJson('MCPlus', 'config', 'channels')

    getConfig('MCPlus', 'config', 'rcon', 'address')
    getConfig('MCPlus', 'config', 'rcon', 'port')
    getConfig('MCPlus', 'config', 'rcon', 'password')
    admin_id = getConfig('MCPlus', 'admin', 'admin', 'admin_id')

    @bot.command(name='mcv')
    async def mcv_command(msg: Message):
        await msg.reply(getMcVersion.get())

    @bot.command(name='server')
    async def server_command(msg: Message, address: str = "0"):
        await msg.reply(getMcServer.getServer(address))

    def is_op(msg: Message, *args) -> bool:
        return msg.author.id == admin_id

    def is_enable_channel(msg: Message, *args) -> bool:
        return msg.ctx.channel.id in channel_id

    @bot.command(name='enable_use', rules=[is_op])
    async def enable_use_command(msg: Message):
        print(is_op(msg))
        if msg.ctx.channel.id not in channel_id:
            channel_id.append(msg.ctx.channel.id)
            pluginJson.writeJson('MCPlus', 'config', 'channels', channel_id)
        await msg.reply(f"{msg.ctx.channel.id}已加入允许的频道列表")
        log.INFO(f"{msg.ctx.channel.id}已加入允许的频道列表", "MCPlus")

    @bot.command(name='wladd', rules=[is_enable_channel])
    async def wladd_command(msg: Message, name: str):
        await msg.reply(runCommand.whitelistAdd(name))

    @bot.command(name='seed', rules=[is_enable_channel])
    async def seed_command(msg: Message):
        await msg.reply(runCommand.seed())

    log.INFO("插件已载入", "MCPlus")
