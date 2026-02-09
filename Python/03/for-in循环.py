
import time

for i in range(3600):
    print('hello,world')
    time.sleep(1)

"""
i 没有用到 可以用_代替
for _ in range(3600):
"""


total = 0
for i in range(1, 101):
    total += i
print(total)


total = 0
for i in range(2, 101, 2):
    if i % 2 == 0:
        total += i
print(total)
