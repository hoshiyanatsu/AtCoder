#!/usr/bin/env python3

x = input().split()
n = int(x[0])
y = int(x[1])

for i in range(n + 1):
  for j in range(n - i + 1):
    if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
      print(i, j, n - i - j)
      exit()
print("-1 -1 -1")

# この問題自力で解けなかった