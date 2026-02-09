"""
二进制、八进制、十进制、十六进制
"""
print(0b100)
print(0o100)
print(100)
print(0x100)

"""
浮点数与科学计数法
"""
print(123.456)
print(1.23456e2)

"""
type()函数可以查看变量的类型
"""
a = 100
b = 123.45
c = 'hello world'
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

"""
变量的类型转换操作
"""
"""
chr()函数可以将整数转成字符,ord()函数可以将字符转成整数  ASCIII码表
"""
"""
bool()转换int()为0/1;str()转换bool()有字符就为1(True),没有字符就为0(False)
"""
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100
