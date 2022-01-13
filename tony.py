from Compiler import Runner
from sys import argv


def main(file):
    run = Runner(filename=file)
    run.run()

def Run():
    name = argv[1]
    main(file = name)

Run()