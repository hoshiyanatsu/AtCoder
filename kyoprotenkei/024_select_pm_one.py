n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

diff_num = 0
for i in range(n):
    diff_num += abs(a_list[i] - b_list[i])

if diff_num > k:
    print("No")
elif diff_num == k:
    print("Yes")
elif (k-diff_num) % 2 == 0:
    print("Yes")
else:
    print("No")