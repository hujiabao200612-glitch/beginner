# 创建集合 {} 没有元素不是集合，而是字典；set() 创建空集合；set() 可以将可迭代对象转换为集合；集合推导式 {表达式 for 变量 in 可迭代对象 if 条件}
set1 = {1, 2, 3, 3, 3, 2}
print(set1)

set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)

set3 = set('hello')
print(set3)

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)
# 集合元素必须是hashable的，因此列表、字典和集合本身不能作为集合的元素，但元组可以作为集合的元素。不可变类型都是hashable的，因此可以作为集合的元素，而可变类型则不能作为集合的元素。

# 元素的遍历
for item in set1:
    print(item)
set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for elem in set1:
    print(elem)

# 成员运算
set1 = {11, 12, 13, 14, 15}
print(10 in set1)      # False
print(15 in set1)      # True
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True

# 二元运算
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}

# 并集
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
print(set1 - set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}

# 对称差
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}

# 复合赋值运算
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
# set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
set1 &= set3
# set1.intersection_update(set3)
print(set1)  # {3, 6}
set2 -= set1
# set2.difference_update(set1)
print(set2)  # {2, 4}

# 比较运算
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

print(set1 < set2)   # True set1 是 set2 的真子集
print(set1 <= set2)  # True set1 是 set2 的子集
print(set2 < set3)   # False set2 和 set3 包含相同的元素，因此 set2 不是 set3 的真子集
print(set2 <= set3)  # True  set2 和 set3 包含相同的元素，因此 set2 是 set3 的子集
print(set2 > set1)   # True set2 是 set1 的超集
print(set2 == set3)  # True set2 和 set3 包含相同的元素，因此 set2 和 set3 是相等的集合

print(set1.issubset(set2))    # True  set1 是 set2 的子集
print(set2.issuperset(set1))  # True  set2 是 set1 的超集

# 添加删除元素
# discard和remove方法都可以用来删除集合中的元素，但它们的行为略有不同。discard方法在删除元素时，如果元素不存在于集合中，它不会引发错误，而是默默地忽略这个操作。而remove方法在删除元素时，如果元素不存在于集合中，它会引发KeyError异常。因此，如果你不确定要删除的元素是否存在于集合中，使用discard方法会更安全一些。
# discard和remove删除后不会返回被删除的元素，而是返回None。如果你需要获取被删除的元素，可以先使用in运算符检查元素是否存在于集合中，然后再使用remove方法删除它，并将被删除的元素保存在一个变量中。例如：

set1 = {1, 10, 100}

# 添加元素
set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}

# 清空元素
set1.clear()
print(set1)  # set()

# 判断是否有相同元素
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True

# 不可变集合 frozenset()可作为set()函数的参数来创建一个不可变集合。frozenset对象是不可变的，因此它不能被修改。一旦创建了一个frozenset对象，就无法添加、删除或修改其中的元素。frozenset对象支持集合的所有操作，如交集、并集、差集和对称差等，但它不支持修改操作，如add()、remove()和clear()等方法。
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False
