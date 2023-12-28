N = int(input())
coins_list = list(map(int, input().split()))
coins_list.sort(reverse=True)
A, B, C = coins_list

min_coins = 9999

for i in range(10000):
    for j in range(10000-i):
        k = (N-A*i-B*j)//C
        if k < 0:
            break
        if A*i + B*j + C*k == N and (i+j+k)<min_coins:
            if i + j + k < min_coins:
                min_coins = i + j + k
    
print(min_coins)