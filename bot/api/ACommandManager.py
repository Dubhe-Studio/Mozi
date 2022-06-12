from khl.command import CommandManager, Lexer, Parser, Command
from typing import List, Union, Pattern
from khl.command.rule import TypeRule

HELP = {}


class ACommandManager(CommandManager):
    def __call__(self,
                 name: str = '',
                 *,
                 help: str = '',
                 desc: str = '',
                 aliases: List[str] = (),
                 prefixes: List[str] = ('/', ),
                 regex: Union[str, Pattern] = '',
                 lexer: Lexer = None,
                 parser: Parser = None,
                 rules: List[TypeRule] = ()):
        args = {
            'help': help,
            'desc': desc,
            'aliases': aliases,
            'prefixes': prefixes,
            'regex': regex,
            'lexer': lexer,
            'parser': parser,
            'rules': rules
        }

        HELP[name] = [help, desc]

        return lambda func: self.add(Command.command(name, **args)(func))
