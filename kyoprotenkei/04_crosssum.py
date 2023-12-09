#!/usr/bin/env python3

H, W = map(int, input().split())
Nums = []
for h in range(H):
    w = list(map(int, input().split()))
    Nums.append(w)

sumgyo = []
sumretsu = []

Ans = []
for i in range(H):
    sum_g = 0
    sum_r = 0
    for j in range(W):
        sum_g += Nums[i][j]
        sum_r += Nums[j][i]
    sumgyo.append(sum_g)
    sumretsu.append(sum_r)

for i in range(H):
    for j in range(W):
        ans = sumgyo[i]+sumretsu[j]-Nums[i][j]
        print(ans, end=" ")
    print()
