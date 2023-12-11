N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

answer = 0
for i in range(N):
    G[i].sort()
    if len(G[i])==1:
        if G[i][0] < i:
            answer += 1
    elif G[i][0]<i and G[i][1]>=i:
        answer += 1
        

print(answer)