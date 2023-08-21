#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci=[]
    if length <= 2:
        for n in range(length):
            fibonacci.append(n)
    elif length>2:
        fibonacci=[0,1]
        while fibonacci.__len__()<length:
            n=(fibonacci[-1]+fibonacci[-2])
            fibonacci.append(n)
    print(fibonacci)
    pass
print_fibonacci(1)