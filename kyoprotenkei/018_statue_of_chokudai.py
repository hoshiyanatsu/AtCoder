import math

T = float(input())
L, X, Y = map(float, input().split())
Q = int(input())
e_list = [float(input()) for _ in range(Q)]

for e in e_list:
    # I / T * 2π を直接計算
    I_radian = e / T * 2 * math.pi
    # Y成分とZ成分を計算
    y_dash = - (L / 2) * math.sin(I_radian)
    z_dash = (L / 2) * (1 - math.cos(I_radian))
    # 2点間の距離を計算
    d = math.sqrt(X**2 + (Y - y_dash)**2)
    # 高さ方向との角度を計算 (atan2 には z, x の順序で渡す)
    theta = math.atan2(z_dash, d)
    # 角度を度数法で出力 (小数点以下12桁まで)
    print(f"{math.degrees(theta):.12f}")