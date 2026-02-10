from rich.table import Table
from rich.console import Console
import random

n = int(input('生成几注双色球号码？'))

red_balls = list(range(1, 34))  # 红球号码范围
blue_balls = list(range(1, 17))  # 蓝球号码范围

for _ in range(n):
    selected_red_balls = []
    for _ in range(6):
        red_ball = random.choice(red_balls)  # 从红球号码中随机选择一个
        selected_red_balls.append(red_ball)  # 将选中的红球添加到列表中
        red_balls.remove(red_ball)  # 从红球号码中移除已选的红球
    selected_red_balls.sort()  # 将选中的红球号码排序

    blue_balls = list(range(1, 17))  # 蓝球号码范围
    blue_ball = random.choice(blue_balls)  # 从蓝球号码中随机选择一个

    for ball in selected_red_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{blue_ball:0>2d}\033[0m')


"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""


# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)
