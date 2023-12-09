#!/usr/bin/env python3

n = int(input())
ts = []
xs = []
ys = []
for i in range(n):
    z = input().split()
    ts.append(int(z[0]))
    xs.append(int(z[1]))
    ys.append(int(z[2]))

x_dash = []
y_dash = []

# 進み方は4^n通り
# すべての配列を用意して一致するものがあったらOKにする？
for i in range(n):
    for j in range(4):
        if j==0:

            x_dash.append(j)
        elif j==1:
        elif j==2:
        elif j==3:
