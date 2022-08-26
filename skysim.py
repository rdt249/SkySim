# Stephen Lawrence 2022

import sys, os

INPUT_PATH = os.getcwd() + '/input.txt'
OUTPUT_PATH = os.getcwd() + '/output.txt'

def main():
    print(INPUT_PATH)
    print(OUTPUT_PATH)

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        for i in range(0,len(args),2):
            if args[i] == '-i': INPUT_PATH = args[i + 1]
            if args[i] == '-o': OUTPUT_PATH = args[i + 1]
    main()
