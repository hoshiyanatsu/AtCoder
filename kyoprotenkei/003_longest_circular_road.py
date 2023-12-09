N = int(input())
G = [[] for _ in range(N)]
# ノード index と繋がっているノードが格納される

for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1 # index = 0から始まるように修正
    G[a].append(b)
    G[b].append(a)

def length(s):
    '''
    ノード s から各ノードまでの長さを求め、リストを返す
    '''
    len_list = [-1] * N
    len_list[s] = 0 # s から s の長さは 0
    stack = [s]
    while (stack): # stack がある限り続ける
        pn = stack.pop() # stackから一つ親ノードを選ぶ
        for cn in G[pn]: # 子ノードをcnとして一つずつ長さを測っていく
            if len_list[cn] == -1:
                stack.append(cn)
                len_list[cn] = len_list[pn] + 1 # 子ノードまでの距離は、親ノードまでの距離 + 1
    return len_list

if __name__=="__main__":
    start_node = 0
    v = max(enumerate(length(start_node)), key=lambda x:x[1])[0] # indexと値を受け取って、値でmaxを検索。そのindexを取得
    v2w_length = max(length(v))
    print(v2w_length+1)