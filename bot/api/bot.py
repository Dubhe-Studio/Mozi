import asyncio
from khl import Bot, Cert, Client, Gateway, HTTPRequester
from bot.api import log
from bot.api.command_manager import ACommandManager
from bot.cli import cli_entry


class ABot(Bot):
    def __init__(self, token: str = '', *, cert: Cert = None, client: Client = None, gate: Gateway = None,
                 out: HTTPRequester = None, compress: bool = True, port=5000, route='/khl-wh'):
        super().__init__(token, cert=cert, client=client, gate=gate, out=out, compress=compress, port=port, route=route)
        self.command = ACommandManager()

    def run(self):
        if not self.loop:
            self.loop = asyncio.get_event_loop()
        try:
            self.loop.run_until_complete(self.start())
        except KeyboardInterrupt:
            cli_entry.stop_plugins()
            log.logger.info('再见')
            log.close()

    def stop(self):
        self.loop.close()
        pass
