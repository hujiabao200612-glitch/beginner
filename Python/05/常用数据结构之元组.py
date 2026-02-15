"""
元组一旦确定，元素不能添加删除和修改，元组的元素可以是任意类型的数据，元组的元素可以重复，元组的元素有序，元组使用小括号()定义。
"""
# 定义一个元组
import timeit
t1 = (1, 2, 3, 4, 5)
t2 = ('a', 2, 3.14, True)

# 查看类型
print(type(t1))
print(type(t2))

# 元组中元素数量
print(len(t1))
print(len(t2))

# 访问元组中的元素
print(t1[0])  # 访问第一个元素
print(t2[1])  # 访问第二个元素
print(t1[-1])  # 访问最后一个元素

# 元组的切片操作
print(t1[1:4])  # 访问索引1到3的元素
print(t2[:3])  # 访问索引0到2的元素
print(t1[::2])  # 访问索引0,2,4的元素
print(t2[::3])

# 遍历元素
for i in t1:
    print(i)

# 成员运算
print(3 in t1)  # 判断3是否在t1中
print(6 in t1)  # 判断6是否在t1中

# 拼接运算 会重复
t3 = t1 + t2
print(t3)

# 比较运算
print(t1 == t2)  # 比较t1和t2是否相等
print(t1 != t2)  # 比较t1和t2是否不相等


# 元组的不可变性
# t1[0] = 10  # 尝试修改元组中的元素，会引发TypeError异常

# 元组的类型
a = ()
b = ('hello')
c = ('hello',)
d = 100
e = (100)
f = (100,)
print(type(a))  # 输出<class 'tuple'>，空元组
print(type(b))  # 输出<class 'str'>，单元素字符串
print(type(c))  # 输出<class 'tuple'>，单元素元组
print(type(d))  # 输出<class 'int'>，单元素整数
print(type(e))  # 输出<class 'int'>，单元素整数
print(type(f))  # 输出<class 'tuple'>，单元素元组

# 打包和解包
t = 1, 2, 3  # 打包，创建一个元组
print(t)  # 输出(1, 2, 3)
a, b, c = t  # 解包，将元组中的元素分别赋值给变量a、b、c
print(a, b, c)  # 输出1 2 3

# 星号表达式 *可以用来捕获剩余的元素，形成一个新的列表
a = 1, 2, 3, 4, 5
i, *j = a  # 将a中的第一个元素赋值给i，剩余的元素赋值给j
print(i, j)  # 输出1 [2, 3, 4, 5]

*i, j = a  # 将a中的最后一个元素赋值给j，剩余的元素赋值给i
print(i, j)  # 输出[1, 2, 3, 4] 5

i, j, *k, l, m, n = a
print(i, j, k, l, m, n)  # 输出1 2 [] 3 4 5

i, j, k, l, m, *n = a
print(i, j, k, l, m, n)  # 输出1 2 3 4 5 []

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

# 交换变量的值
a, b = b, a
a, b, c = c, a, b

# 元组和列表的比较
print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

# 元组和列表转换
infos = ('骆昊', 45, True, '四川成都')
# 将元组转换成列表
print(list(infos))  # ['骆昊', 45, True, '四川成都']

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')
