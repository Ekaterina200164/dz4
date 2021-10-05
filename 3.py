import argparse
import sys
from pathlib import Path
fib1 = 1
fib2 = 1
fib = []
fib.append(fib1)
fib.append(fib2)
parser = argparse.ArgumentParser()
parser.add_argument('--output_file', nargs = 1)
parser.add_argument('--all','-a', nargs = "?", default = 0)
parser.add_argument('--file','-f', nargs = "?", default = 0)
for i in range(2, int(sys.argv[1])):
    fib1, fib2 = fib2, fib1 + fib2
print(fib2)
for i in sys.argv:
    if i == '-a':
        fib1 = fib2 = 1
        print(fib1, fib2, end = ' ')
        for i in range(2, int(sys.argv[1])):
            fib1, fib2 = fib2, fib1 + fib2
            print(fib2, end = ' ')
            fib.append(fib2)
        print()
    if i == '-f':
        answ3 = Path('answ3.txt')
        answ3.write_text(str(fib)) 
