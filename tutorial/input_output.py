#!/usr/local/bin/python3
import math
import pprint, pickle

s = 'Hello, Hu'
print(str(s))
print(repr(s))
print(str(1 / 7))
x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)
#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, Hu\n'
hellos = repr(hello)
print(hello)
print(hellos)
# repr() 的参数可以是 Python 的任何对象
print(repr((x, y, ('Google', 'Hu'))))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('12'.zfill(5))

print('-3.14'.zfill(7))

print('3.14159265359'.zfill(5))

print('{}网址： "{}!"'.format('教程', 'www.Hu.com'))

print('{0} 和 {1}'.format('Google', 'Hu'))

print('{1} 和 {0}'.format('Google', 'Hu'))

print('{name}网址： {site}'.format(name='教程', site='www.Hu.com'))

print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Hu', other='Taobao'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('常量 PI 的值近似为： {}。'.format(math.pi))

print('常量 PI 的值近似为： {!a}。'.format('a'))

print('常量 PI 的值近似为： {!s}。'.format(math.pi))

print('常量 PI 的值近似为： {!r}。'.format(math.pi))

print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

table = {'Google': 1, 'Hu': 2, 'Taobao': 3}

for name, number in table.items():
    print('{0:8} ==> {1:5d}'.format(name, number))

'''
如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
'''
print('Hu: {0[Hu]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# 也可以通过在 table 变量前使用 '**' 来实现相同的功能
print('Hu: {Hu:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

print(data1)

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

print(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()


class Base:
    def myMethod(self):
        print("调用超类方法")

class Parent(Base):  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法

p = Parent()
p.myMethod()
super(Parent, p).myMethod()