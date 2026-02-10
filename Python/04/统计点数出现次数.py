import random

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0

for i in range(1, 6001):
    dice = random.randint(1, 6)
    if dice == 1:
        f1 += 1
    elif dice == 2:
        f2 += 1
    elif dice == 3:
        f3 += 1
    elif dice == 4:
        f4 += 1
    elif dice == 5:
        f5 += 1
    else:
        f6 += 1
print(f'1点出现了{f1}次，2点出现了{f2}次，3点出现了{f3}次，4点出现了{f4}次，5点出现了{f5}次，6点出现了{f6}次')


counters = [0] * 6  # 创建一个长度为6的列表，初始值为0
for i in range(1, 6001):
    dice = random.randint(1, 6)
    counters[dice - 1] += 1  # 根据骰子的点数更新对应的计数器

print(f'1点出现了{counters[0]}次，2点出现了{counters[1]}次，3点出现了{counters[2]}次，4点出现了{counters[3]}次，5点出现了{counters[4]}次，6点出现了{counters[5]}次')