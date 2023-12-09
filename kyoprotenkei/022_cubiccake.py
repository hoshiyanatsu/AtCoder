import math
a, b, c = map(int, input().split())

gcd = math.gcd(a, b)
gcd = math.gcd(gcd, c)

a = a//gcd - 1
b = b//gcd - 1
c = c//gcd - 1

print(a+b+c)