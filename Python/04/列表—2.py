"""
添加删除元素
"""
# append()方法在列表末尾添加元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('ducati')
print(bicycles)
# insert()方法在列表的指定位置添加元素
bicycles.insert(0, 'ducati')
print(bicycles)
# remove()方法根据值删除列表中的元素
if 'ducati' in bicycles:
    bicycles.remove('ducati')
# pop()方法根据索引删除列表中的元素,如果不指定索引，默认删除最后一个元素
bicycles.pop()
bicycles.pop(2)
print(bicycles)
# clear()方法清空列表中的所有元素
bicycles.clear()


"""
元素位置和频次
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles.index('redline'))  # index()方法返回列表中第一个匹配项的索引
print(bicycles.index('redline', 1))  # index()方法可以指定起始位置
print(bicycles.count('redline'))  # count()方法返回列表中某个   


"""
元素排序和反转
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.sort()  # sort()方法对列表进行永久排序
print(bicycles)
bicycles.reverse()  # reverse()方法对列表进行永久反转
print(bicycles)

"""
列表生成式
"""
items = []
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        items.append(i)
print(items)

items = [i for i in range(1,100) if i % 3 == 0 and i % 5 == 0]
print(items)  



nums1 = [35, 12, 97, 64, 55]
nums2 = []

for i in nums1:
        nums2.append(i**2)
print(nums2)

nums2 = [i**2 for i in nums1]
print(nums2)



nums1 = [35, 12, 97, 64, 55]
nums2 = []

for i in nums1:
     if i > 50:
          nums2.append(i)
print(nums2)

nums2 = [i for i in nums1 if i > 50]
print(nums2)

"""
嵌套的列表
"""
scores = [[85, 92, 78], [90, 88, 95], [80, 85, 82]]
print(scores[0])  # 访问第一行
print(scores[1][2])  # 访问第二行第三列的元素

scores = []
for _ in range(3):
    row = []
    for _ in range(3):
        score = int(input('请输入一个成绩: '))
        row.append(score)
    scores.append(row)

#随机成绩
import random

scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(3)]