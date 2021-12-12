from Lexer import lexer
from Lexer import Compiler


def run():
    file = open("new.io", 'r').read()
    runner = lexer(data=file)
    runner.tokenizer()
    runner.Parser()
    compile = Compiler(node=runner.node)
    compile.Eval()

run()
