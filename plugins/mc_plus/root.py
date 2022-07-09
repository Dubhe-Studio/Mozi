from bot.api.plugin_config import get_config
from plugins.mc_plus.lib import get_mc_server, get_mc_version, run_command
from bot.cli.cli_entry import bot
from bot.api import log, plugin_json
from khl import Message

pluginName = "MCPlus"


def on_start():
    config = plugin_json.PluginJson(plugin=pluginName)
    channel_id = config.read("channels")

    get_config(pluginName, 'config', 'rcon', 'address')
    get_config(pluginName, 'config', 'rcon', 'port')
    get_config(pluginName, 'config', 'rcon', 'password')
    admin_id = get_config(pluginName, 'admin', 'admin', 'admin_id')

    @bot.command(name='mcv', help='/mcv', desc='查询最新的Minecraft版本')
    async def mcv_command(msg: Message):
        await msg.reply(await get_mc_version.get())

    @bot.command(name='server', help='/server', desc='获取某服务器的信息')
    async def server_command(msg: Message, address: str = "0"):
        await msg.reply(await get_mc_server.get_server(address))

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
            await msg.reply(run_command.whitelist_add(name))

    @bot.command(name='seed', help='/seed', desc='查询服务器种子')
    async def seed_command(msg: Message):
        if is_enable_channel(msg):
            await msg.reply(run_command.seed())

    @bot.command(name='time', help='/time', desc='查询服务器时间')
    async def time_command(msg: Message):
        if is_enable_channel(msg):
            await msg.reply(run_command.time())

    log.info(pluginName, "插件已载入")


def onStop():
    ...
