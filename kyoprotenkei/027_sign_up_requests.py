N = int(input())
name_dict = {}
for i in range(N):
    s = input()
    if name_dict.get(s):
        pass
    else:
        name_dict[s] = i+1

name_dict_swap = {v: k for k, v in name_dict.items()}

for i in range(1, N+1):
    if name_dict_swap.get(i):
        print(i)