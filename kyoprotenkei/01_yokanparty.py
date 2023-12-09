#!/usr/bin/env python3
n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))


def solve(m: int):
    cnt = 0
    pre = 0
    for i in range(n):
        if a[i] - pre >= m and l - a[i] >= m:
            cnt += 1
            pre = a[i]
    if cnt >= k:
        return True
    return False

def main():
    # 二分探索法で解く
    left = -1
    right = l + 1
    while right - left > 1:
        mid = int(left + ((right - left) / 2))
        if solve(m=mid) == False:
            right = mid
        else:
            left = mid
    print(left)


if __name__ == "__main__":
    main()