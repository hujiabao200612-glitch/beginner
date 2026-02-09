import math

a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'三角形的周长是：{perimeter:.2f}')
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'三角形的面积是：{area:.2f}')
else:
    print('无法构成三角形！')
