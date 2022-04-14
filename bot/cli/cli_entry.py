import asyncio

from khl import Bot, Message
from bot.api import getConfig, pluginsManager, log

pluginsManager = pluginsManager.pluginsManager()
token = getConfig.getConfig("settings", "token")
help:list[str] = []


class aBot(Bot):
    pass

    def run(self):
        if not self.loop:
            self.loop = asyncio.get_event_loop()
        try:
            self.loop.run_until_complete(self.start())
        except KeyboardInterrupt:
            pluginsManager.stopPlugins()
            log.logger.info('再见')
            log.close()

    def stop(self):
        self.loop.close()
        pass


bot = aBot(token=token)


def entry_point():
    help.append("/help\t显示帮助")
    help_text = ""
    pluginsManager.runPlugins()
    for i in range(len(help)):
        if i == 0:
            help_text = help[0]
        else:
            help_text = help_text + '\n' + help[i]

    @bot.command(name='help')
    async def help_command(msg: Message):
        await msg.reply(help_text)

    log.logger.info("机器人已启动")
    bot.run()

