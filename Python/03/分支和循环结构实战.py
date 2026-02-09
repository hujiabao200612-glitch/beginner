"""
斐波那契数列（20个）
"""

import random
num1 = 1
num2 = 1
print(num1, num2, end=' ')
for i in range(3, 21):
    num3 = num1 + num2
    print(num3, end=' ')
    num1, num2 = num2, num3
print()


"""
寻找水仙花数
"""
for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i, end=' ')
print()


"""
百钱百鸡问题
"""
for x in range(0, 21):
    for y in range(0, 100-x):
        z = 100 - x - y
        if z % 3 == 0 and 5*x + 3*y + z//3 == 100:
            print(f'公鸡{x}只，母鸡{y}只，小鸡{z}只')
print()


"""
CRAPS赌博游戏
"""
money = 1000

while money > 0:
    bet = int(input('请输入赌注金额：'))
    if bet > money or bet <= 0:
        print('请重新输入一个有效的赌注金额！')
        continue

    first_dice1 = random.randint(1, 6)
    first_dice2 = random.randint(1, 6)
    first_dice_sum = first_dice1 + first_dice2
    print(f'掷出的骰子点数为：{first_dice1} 和 {first_dice2}，总和为 {first_dice_sum}')
    if first_dice_sum == 7 or first_dice_sum == 11:
        print('你赢了！')
        money += bet
    elif first_dice_sum == 2 or first_dice_sum == 3 or first_dice_sum == 12:
        print('你输了！')
        money -= bet
    else:
        while True:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice_sum = dice1 + dice2
            print(f'掷出的骰子点数为：{dice1} 和 {dice2}，总和为 {dice_sum}')
            if dice_sum == first_dice_sum:
                print('你赢了！')
                money += bet
                break
            elif dice_sum == 7:
                print('你输了！')
                money -= bet
                break

print('游戏结束，你的资金已经用完了！')
