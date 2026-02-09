import math
r = float(input('请输入一个圆的半径：'))
area = math.pi * r * r
perimeter = 2 * math.pi * r

print('圆的面积是：%.2f' % area)
print('圆的周长是：%.2f' % perimeter)
