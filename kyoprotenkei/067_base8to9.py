
def eight2ten(n_list:list) -> int:
    l = len(n_list)
    n10 = 0
    i = 0
    for _ in range(l):
        x = n_list.pop()
        n10 += x*8**i
        i += 1

    return n10

def ten2nine(n:int) -> list:
    sisuu = 0
    while (n//(9**sisuu)>0):
        sisuu += 1

    n9_list = []
    for i in reversed(range(sisuu)):
        if i==0:
            n9_list.append(n)
        elif n//(9**i)==0:
            n9_list.append(0)
        else:
            n9_list.append(n//(9**i))
            n -= (n//(9**i))*9**i

    return n9_list

def numbers_eight2five(n_list:list) -> list:
    for i in range(len(n_list)):
        if n_list[i]==8:
            n_list[i] = 5

    return n_list

N, K = map(int, input().split())

N_list = list(str(N))
N_list = [int(x) for x in N_list]

n10 = eight2ten(N_list)
n9list = ten2nine(n10)
n8_list = numbers_eight2five(n9list)

for _ in range(K-1):
    n10 = eight2ten(n8_list)
    n9list = ten2nine(n10)
    n8_list = numbers_eight2five(n9list)

if n8_list==[]:
    print(0)
else:
    print(*n8_list, sep="")