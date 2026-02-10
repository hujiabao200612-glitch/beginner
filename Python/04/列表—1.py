"""
list() 函数可以将一个可迭代对象转换为列表。
在这个例子中，我们使用 range() 函数生成一个从 1 到 10 的整数序列，并将其转换为一个列表。    
"""
items = list(range(1, 11))
print(items)

"""
运算
"""
numbers = list(range(1, 11))
numbers2 = list(range(8, 18))
print(numbers + numbers2)  # 列表连接
print(numbers * 2)  # 列表重复
print(8 in numbers)  # 成员资格测试
print(15 in numbers)  # 成员资格测试
print(15 not in numbers)  # 成员资格测试

print(numbers[0:5:2])
numbers[1:3] = [20, 30]  # 切片赋值, 将索引 1 和 2 的元素替换为 20 和 30

print(numbers == numbers2)  # 列表比较
print(numbers != numbers2)  # 列表比较
print(numbers < numbers2)  # 列表比较


"""
遍历
"""
for i in range(len(numbers)):
    print(numbers[i])

for item in numbers:
    print(item)
