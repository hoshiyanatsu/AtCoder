#!/usr/bin/env python3

x = input().split()
a = int(x[0])
b = int(x[1])

if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
