#!/usr/bin/env python3


def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    q = int(input())
    b = [int(input()) for _ in range(q)]

    for j in range(q):
        left = 0
        right = n - 1
        while right - left > 1:
            mid = int(left + (right - left) / 2)

            if b[j] < a[mid]:
                right = mid
            else:
                left = mid
        if abs(a[left] - b[j]) < abs(a[right] - b[j]):
            print(abs(a[left] - b[j]))
        else:
            print(abs(a[right] - b[j]))


if __name__ == "__main__":
    main()
