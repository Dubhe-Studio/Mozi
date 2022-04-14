from bot.api import log
from plugins.ConvenienceFunction.lib import getAnimeImage, getSentence, getYulu, getToday, getJoke, getWeather, getMusic
from bot.cli.cli_entry import bot, help
from khl import Message


def onStart():
    help.append("=======================================")
    help.append("/joke\t笑话")
    help.append("/stl <pe|pc>\t获取一张二次元美图")
    help.append("/tq <city>\t获取某城市天气")
    help.append("/music <name>\t点歌")
    help.append("/yl\t社会语录")
    help.append("/lsjt\t历史今天")
    help.append("/yy\t一言")

    @bot.command(name='yl')
    async def yl_command(msg: Message):
        await msg.reply(getYulu.get())

    @bot.command(name='lsjt')
    async def lsjt_command(msg: Message):
        await msg.reply(getToday.get())

    @bot.command(name='yy')
    async def yy_command(msg: Message):
        await msg.reply(getSentence.get())

    @bot.command(name='joke')
    async def joke_command(msg: Message):
        await msg.reply(getJoke.get())

    @bot.command(name='stl')
    async def stl_command(msg: Message, img_type: str = "pc"):
        await msg.reply(getAnimeImage.get(img_type))

    @bot.command(name='tq')
    async def tq_command(msg: Message, city: str = "0"):
        await msg.reply(getWeather.getWeather(city).repr)

    @bot.command(name='music')
    async def music_command(msg: Message, name: str = "0"):
        await msg.reply(getMusic.getMusic(name))

    log.info("便民功能", "插件已载入")
