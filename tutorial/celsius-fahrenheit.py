#!/usr/local/bin/python3

# -*-coding:utf-8-*-

# @Author: hugheslou
# @Time: 2018/5/17 00:12


# 用户输入摄氏温度

# 接收用户输入
celsius = float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))