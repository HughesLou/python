#!/usr/local/bin/python3

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "Huuuu"  # 字符串

print(counter)
print(miles)
print(name)

a = b = c = 1

print(a)
print(b)
print(c)

a, b, c = 1, 2, "Huuuu"

print(a)
print(b)
print(c)

# Python3 支持 int、float、bool、complex（复数）
a, b, c, d = 20, 5.5, True, 4 + 3j

print(type(a), type(b), type(c), type(d))

isinstance(a, int)

# isinstance 和 type 的区别
'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''


class A:
    pass


class B(A):
    pass


isinstance(A(), A)  # returns True
type(A()) == A  # returns True
isinstance(B(), A)  # returns True
type(B()) == A  # returns False

# 当指定一个值时，Number 对象就会被创建
var1 = 1
var2 = 10

# 可以使用del语句删除一些对象引用
del var1

# 数值运算
'''
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。
'''
print(2 / 4)
print(2 // 4)
print(2 * 4)
print(2 ** 4)

# Python 没有单独的字符类型，一个字符就是长度为1的字符串
# Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误
# 字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
word = 'Python'
print(word[0], word[5])

# List
list = ['abcd', 786, 2.23, 'Hu', 70.2]
tinylist = [123, 'Hu']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

# 与Python字符串不一样的是，列表中的元素是可以改变的
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
print(a)
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []  # 将对应的元素值设置为 []
print(2)

# Tuple
tuple = ('abcd', 786, 2.23, 'Hu', 70.2)
tinytuple = (123, 'Hu')

tuple1 = 'abcd', 786, 2.23, 'Hu', 70.2
print(tuple1)

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

# Set
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abcdef')
b = set('abcxyz')

print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素

# Dictionary
dict = {}
dict['one'] = "1 - 教程"
dict[2] = "2 - 工具"

tinyDict = {'name': 'Hu', 'code': 1, 'site': 'www.hu.com'}
tinyDict1 = {'name': 'Hu', 3: 1, 'site': 'www.hu.com'}

print(tinyDict1[3])

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinyDict)  # 输出完整的字典
print(tinyDict.keys())  # 输出所有键
print(tinyDict.values())  # 输出所有值

print(dict([('Hu', 1), ('Google', 2), ('Taobao', 3)]))
print({x: x ** 2 for x in (2, 4, 6)})
print(dict(Hu=1, Google=2, Taobao=3))
