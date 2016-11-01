import sys
import argparse
import os

parser = argparse.ArgumentParser(
    description='Дерево файловой системы'
)

parser.add_argument(
    '--folders_only',
    action='store_true'
)

parser.add_argument(
    '-i',
    '--include',
    metavar='VALUE',
    type=str,
    action='store'
)

parser.add_argument(
    '-e',
    '--exclude',
    metavar='VALUE',
    type=str,
    action='store'
)

parser.add_argument(
    '-a',
    '--all',
    action='store_true'
)

parser.add_argument(
    '--full_name',
    action='store_true'
)

parser.add_argument(
    'values',
    metavar='VALUES',
    nargs="+"
)

args = parser.parse_args()

need_dir = args.values[0]

def print_directory(cwd,k):
    os.chdir(cwd)
    for i in range(k):
        print(' ',end='')
    print(cwd[cwd.rfind('/')+1:])
    ways = os.listdir(cwd)
    for elem in ways:
        if os.path.isfile(cwd+'/'+elem):
            for i in range(k+2):
                print(' ',end='')
            print(elem)
    for elem in ways:
        if os.path.isdir(cwd+'/'+elem):
            print_directory(cwd+'/'+elem,k+2)
        os.chdir(cwd)
print(need_dir)
print_directory(need_dir,1)
