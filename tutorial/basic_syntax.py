#!/usr/local/bin/python3
import keyword
import sys
from sys import argv, path

print("Hello World")

# python保留字
print(keyword.kwlist)

# 注释
'''
comment
comment
'''

"""
comment
comment
"""

# 行与缩进
if True:
    print("True")
elif True:
    print("False")
else:
    print("None")

# 多行语句
total = 'item_one' + \
        'item_two' + \
        'item_three'

total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

# 数字
True
-2.3E-5
1.2 + 2j

# 字符串
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

str = 'Huopity'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nHu')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nHu')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 等待用户输入
input("\n\n按下 enter 键后退出")

# 同一行显示多条语句
x = 'Hu';
sys.stdout.write(x + '\n')

# Print 输出
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

# import 与 from...import
print('================Python import mode==========================');
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

print('================python from import===================================')
print('argv:', argv)
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

print(dir(sys))

print(dir())