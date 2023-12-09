N = int(input())
class_1_points = [0] * (N+1)
class_2_points = [0] * (N+1)

for i in range(N):
    i = i+1
    c, p = map(int, input().split())
    if c==1:
        class_1_points[i] = p
    else:
        class_2_points[i] = p

class_1_sum_points = [0] * (N+1)
class_2_sum_points = [0] * (N+1)

class1_sum = 0
class2_sum = 0
for i in range(N+1):
    class1_sum += class_1_points[i]
    class2_sum += class_2_points[i]

    class_1_sum_points[i] = class1_sum
    class_2_sum_points[i] = class2_sum

Q = int(input())
L_R_list = [map(int, input().split()) for _ in range(Q)]

for l, r in L_R_list:
    answer1 = class_1_sum_points[r]-class_1_sum_points[l-1]
    answer2 = class_2_sum_points[r]-class_2_sum_points[l-1]
    print(answer1, answer2)
