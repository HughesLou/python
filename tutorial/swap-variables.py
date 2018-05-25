#!/usr/local/bin/python3

# -*-coding:utf-8-*-

# @Author: hugheslou
# @Time: 2018/5/17 00:12

# 用户输入

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))
