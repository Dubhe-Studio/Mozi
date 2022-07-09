from bot.api import log
from plugins.convenience_function.lib import get_animeImage, get_sentence, get_yulu, get_today, get_joke, get_weather, get_music
from bot.cli.cli_entry import bot
from khl import Message

pluginName = "便民功能"


def on_start():
    @bot.command(name='yl', help='/yl', desc='社会语录')
    async def yl_command(msg: Message):
        await msg.reply(get_yulu.get())

    @bot.command(name='lsjt', help='/lsjt', desc='历史今天')
    async def lsjt_command(msg: Message):
        await msg.reply(get_today.get())

    @bot.command(name='yy', help='/yy', desc='一言')
    async def yy_command(msg: Message):
        await msg.reply(get_sentence.get())

    @bot.command(name='joke', help='/joke', desc='笑话')
    async def joke_command(msg: Message):
        await msg.reply(get_joke.get())

    @bot.command(name='stl', help='/stl', desc='获取一张二次元美图')
    async def stl_command(msg: Message, img_type: str = "pc"):
        await msg.reply(get_animeImage.get(img_type))

    @bot.command(name='tq', help='/tq', desc='获取某城市天气')
    async def tq_command(msg: Message, city: str = "0"):
        await msg.reply(get_weather.get_weather(city))

    @bot.command(name='music', help='/music', desc='点歌')
    async def music_command(msg: Message, name: str = "0"):
        await msg.reply(get_music.get_music(name))

    log.info(pluginName, "插件已载入")


def onStop():
    ...
