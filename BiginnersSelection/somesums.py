#!/usr/bin/env python3

x = input().split()
n = int(x[0])
a = int(x[1])
b = int(x[2])
num_li = []
sums = 0

for i in range(n):
    sum = 0
    num = i+1
    for j in range(len(str(num))):
        sum += int(str(num)[-j-1])
    if a <= sum <= b:
        num_li.append(num)
for i in range(len(num_li)):
    sums += num_li[i]

print(sums)