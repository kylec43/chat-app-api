import sys, os
sys.path.append(os.path.abspath(".."))
from cli_tool.actions.create_module import create_module

def main(args):
    if (len(args) < 1):
        print('Invalid Action: Type "help" for help.')
        return

    action = args[0]

    if (action == 'help'):
        print('Actions:')
        print('create_module [name]')
    elif (action == 'create_module'):
        if len(args) < 2:
            print('Missing module name')
            return
        module_name = args[1]
        create_module(module_name)
        


if __name__ == "__main__":
   main(sys.argv[1:])