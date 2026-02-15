# 创建字典 {}，每个元素由：键（key）和值（value）组成，键与值之间用冒号分隔，元素之间用逗号分隔
# 字典中的键必须是唯一的，值可以重复
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101',
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person)
# 用dict()函数创建字典,用zip()压缩两个序列
keys = ['name', 'age', 'height', 'weight', 'addr', 'tel', 'emergence contact']
values = ['王大锤', 55, 168, 60, '成都市武侯区科华北路62号1栋101',
          '13122334455', '13800998877']
person1 = dict(zip(keys, values))
print(person1)
person = dict(name='王大锤', age=55, height=168,
              weight=60, addr='成都市武侯区科华北路62号1栋101')
# {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person)
# 用字典生成式创建字典
person2 = {k: v for k, v in zip(keys, values)}
print(person2)  # {'name': '王大锤', 'age':

# 遍历、求长度
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101'
}
print(len(person))  # 5
for value in person.values():
    print(value)  # 王大锤 55 168 60 成都市武侯区科华北路62号1栋101
for key in person.keys():
    print(key)  # name age height weight addr

# 键必须是不可变类型，值可以是
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person)


# 成员运算与索引运算
person = {'name': '王大锤', 'age': 55, 'height': 168,
          'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 成员运算
print('name' in person)  # True
print('tel' in person)   # False

# 索引运算  没有值是引发KeyError
print(person['name'])
print(person['addr'])
person['age'] = 25
person['height'] = 178
person['tel'] = '13122334455'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')

# 字典的方法
# get 错误返回None
person = {'name': '王大锤', 'age': 25,
          'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))       # 王大锤
print(person.get('sex'))        # None
print(person.get('sex', True))  # True
# keys values items(键值组成二元组输出)
person = {'name': '王大锤', 'age': 25, 'height': 178}
print(person.keys())    # dict_keys(['name', 'age', 'height'])
print(person.values())  # dict_values(['王大锤', 25, 178])
# dict_items([('name', '王大锤'), ('age', 25), ('height', 178)])
print(person.items())
for key, value in person.items():
    print(f'{key}:\t{value}')
# x.update(y)或者|,y补充或者替换x中的值或键值
person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person1.update(person2)
# {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person1)
person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person1 |= person2
# {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person1)
# pop或popitem方法从字典中删除元素，默认删除最后，前者会返回（获得）键对应的值，但是如果字典中不存在指定的键，会引发KeyError错误；后者在删除元素时，会返回（获得）键和值组成的二元组。clear方法会清空字典中所有的键值对
person = {'name': '王大锤', 'age': 25,
          'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('age'))  # 25
# {'name': '王大锤', 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person)
print(person.popitem())   # ('addr', '成都市武侯区科华北路62号1栋101')
print(person)             # {'name': '王大锤', 'height': 178}
person.clear()
print(person)             # {}

# del关键字，在删除元素的时候如果指定的键索引不到对应的值，一样会引发KeyError错误
person = {'name': '王大锤', 'age': 25,
          'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
del person['age']
del person['addr']
print(person)  # {'name': '王大锤', 'height': 178}

# 应用  输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。
sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
sorted_keys = sorted(counter, key=counter.get, reverse=True)
for key in sorted_keys:
    print(f'{key} 出现了 {counter[key]} 次.')

# 应用  在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
