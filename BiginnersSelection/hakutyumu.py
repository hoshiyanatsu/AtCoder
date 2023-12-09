#!/usr/bin/env python3

s = input()
s_ = s
t = ""
t_list = ['dream', 'dreamer', 'erase', 'eraser']

for i in range(int(len(s)/5)+1):
    if t == s:
        print("YES")
        exit()
    else :
        for word in t_list:
            # 後方一致
            if s_.endswith(word):
                t = word + t
                s_ = s_[0:-len(word)]

print("NO")