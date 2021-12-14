from Lexer import lexer
from Lexer import Node
from Lexer import Compiler

def run():
    file = open("new.io", 'r').read()
    runner = lexer(data=file)
    runner.tokenizer()
    node = Node(tokens=runner.tokens)
    node.noder()
    compile_code = Compiler(node=node.node)
    compile_code.Compile()


run()
