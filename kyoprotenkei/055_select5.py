import itertools

N, P, Q = map(int, input().split())
a_list = list(map(int, input().split()))

answer = 0
for i in range(0, N):
    for j in range(0, i):
        for k in range(0, j):
            for l in range(0, k):
                for m in range(0, l):
                    if (a_list[i]*a_list[j]%P * a_list[k]%P * a_list[l]%P * a_list[m]%P) == Q:
                        answer += 1

print(answer)

# pypy で提出すると通る。CPythonだとTLE。