#!/usr/bin/env python3

n = int(input())
ds = []
counter = 0

for i in range(n):
    d = int(input())
    ds.append(d)

for i in range(len(ds)):
    if ds != []:
        for i in range(len(ds)):
            # 半径の中で一番大きいものを取得
            big = int(ds[0])
            for num in ds:
                if int(num) > big:
                    big = int(num)
        ds = [d for d in ds if d!=big]
        counter += 1
    else:
        break
print(counter)