import argparse
import sys
fib1 = 1
fib2 = 1
parser = argparse.ArgumentParser()
parser.add_argument('--value', nargs = 1)
for i in range(2, int(sys.argv[1])):
    fib1, fib2 = fib2, fib1 + fib2
print(fib2) 
