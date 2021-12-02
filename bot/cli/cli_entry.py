import os
import datetime
from bot.lib import Bot, Message
from bot.api import log, getConfig, runPuglins, pro_dir

token = getConfig.getConfig("settings", "token")
bot = Bot(token=token)
help = []


def entry_point():
    if os.path.isfile(pro_dir+'\\logs\\latest.log'):
        os.rename(pro_dir+'\\logs\\latest.log', pro_dir+'\\logs\\{}.log'.format(datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y-%m-%d-%H-%M-%S')))
    help.append("/help\t显示帮助")
    help_text = ""
    runPuglins.runPlugins()
    for i in range(len(help)):
        if i == 0:
            help_text = help[0]
        else:
            help_text = help_text + '\n' + help[i]

    @bot.command(name='help')
    async def help_command(msg: Message):
        await msg.reply(help_text)

    log.INFO("机器人已启动")
    bot.run()
