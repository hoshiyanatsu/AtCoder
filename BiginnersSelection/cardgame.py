#!/usr/bin/env python3

n = int(input())
cards = input().split()
alice = []
bob = []

for i in range(n):
    # カードの中で一番大きいものを取得
    big = int(cards[0])
    for num in cards:
        if int(num) > big:
            big = int(num)
    if i % 2 == 0:
        alice.append(big)
        cards.remove(str(big))
    else:
        bob.append(big)
        cards.remove(str(big))
sum_a = 0
sum_b = 0
# 合計値を求める
for num in alice:
    sum_a += num
for num in bob:
    sum_b += num

print(sum_a - sum_b)
