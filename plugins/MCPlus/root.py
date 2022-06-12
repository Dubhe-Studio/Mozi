from bot.api.pluginConfig import getConfig
from plugins.MCPlus.lib import getMcServer, getMcVersion, runCommand
from bot.cli.cli_entry import bot
from bot.api import log, pluginJson
from khl import Message

pluginName = "MCPlus"


def onStart():
    config = pluginJson.pluginJson(plugin=pluginName)
    channel_id = config.read("channels")

    getConfig(pluginName, 'config', 'rcon', 'address')
    getConfig(pluginName, 'config', 'rcon', 'port')
    getConfig(pluginName, 'config', 'rcon', 'password')
    admin_id = getConfig(pluginName, 'admin', 'admin', 'admin_id')

    @bot.command(name='mcv', help='/mcv', desc='查询最新的Minecraft版本')
    async def mcv_command(msg: Message):
        await msg.reply(await getMcVersion.get())

    @bot.command(name='server', help='/server', desc='获取某服务器的信息')
    async def server_command(msg: Message, address: str = "0"):
        await msg.reply(await getMcServer.getServer(address))

    def is_op(msg: Message) -> bool:
        return msg.author.id == admin_id

    def is_enable_channel(msg: Message) -> bool:
        return msg.ctx.channel.id in channel_id

    @bot.command(name='enable_use', help='/enable_use', desc='允许当前频道使用')
    async def enable_use_command(msg: Message):
        if is_op(msg):
            if msg.ctx.channel.id not in channel_id:
                channel_id.append(msg.ctx.channel.id)
                config.write('channels', channel_id)
            await msg.reply(f"{msg.ctx.channel.id}已加入允许的频道列表")
            log.info(pluginName, f"{msg.ctx.channel.id}已加入允许的频道列表")

    @bot.command(name='wladd', help='/wladd', desc='为自己添加服务器白名单')
    async def wladd_command(msg: Message, name: str):
        if is_enable_channel(msg):
            await msg.reply(runCommand.whitelistAdd(name))

    @bot.command(name='seed', help='/seed', desc='查询服务器种子')
    async def seed_command(msg: Message):
        if is_enable_channel(msg):
            await msg.reply(runCommand.seed())

    log.info(pluginName, "插件已载入")


def onStop():
    ...
