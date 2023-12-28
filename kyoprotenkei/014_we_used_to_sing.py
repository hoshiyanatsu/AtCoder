import math

N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort()

huben = 0
for i in range(N):
    huben += abs(a_list[i]-b_list[i])

print(huben)