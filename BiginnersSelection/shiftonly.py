#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

even = True
count = 0
while even:
    for i, a in enumerate(A):
        if a % 2 == 0:
            A[i] = a / 2
        else:
            even = False
    if even:
        count += 1
print(count)


# n = int(input())
# an = input().split()
# even = True
# counter = 0
# while even==True:
#     for i in range(n):
#         ai = int(an[i])
#         if ai %2 ==0:
#             an[i] = ai/2
#         else:
#             even = False
#     if even == True:
#         counter += 1

# print(counter)
