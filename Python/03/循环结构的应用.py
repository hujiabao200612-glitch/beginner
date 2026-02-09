import random
num = int(input('请输入一个整数：'))
count = 0

for i in range(2, num - 1):
    if num % i == 0:
        count = 1
        break
if count == 0:
    print(f'{num}是一个素数')
else:
    print(f'{num}不是一个素数')


num1 = int(input('请输入一个整数：'))
num2 = int(input('请输入另一个整数：'))

for i in range(2, num1+1):
    if num1 % i == 0 and num2 % i == 0:
        count = i
print(f'{num1}和{num2}的最大公约数是{count}')


answer = random.randrange(1, 101)
count = 0

while True:
    num = int(input('请输入一个整数:'))
    count += 1
    if num > answer:
        print('大了')
    elif num < answer:
        print('小了')
    else:
        print(f'猜对了')
        break
print(f'你一共猜了{count}次.')
