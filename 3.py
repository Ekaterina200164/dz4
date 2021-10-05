import argparse
import sys
from pathlib import Path
fib1 = 1
fib2 = 1
fib = []

parser = argparse.ArgumentParser()
parser.add_argument('--value', nargs = 1)
parser.add_argument('--all','-a', nargs = "?", default = 0)
parser.add_argument('--file','-f', nargs = "?", default = 0)

for i in range(2, int(sys.argv[1])):
    fib1, fib2 = fib2, fib1 + fib2
print(fib2)

if '-a' in sys.argv:
    if int(sys.argv[1]) == 1: 
        fib.append(1)
        print(*fib)
    elif int(sys.argv[1]) == 2:
        fib.append(1)
        fib.append(1)
        print(*fib)
    else:
        fib1 = fib2 = 1
        fib.append(1)
        fib.append(1)
        print(fib1, fib2, end = ' ')
        for i in range(2, int(sys.argv[1])):
            fib1, fib2 = fib2, fib1 + fib2
            print(fib2, end = ' ')
            fib.append(fib2)
        print()

if '-f' in sys.argv:
    answ3 = Path('answ3.txt')
    answ3.write_text(str(fib2) + '\n' +' '.join(map(str, fib)) + '\n')
