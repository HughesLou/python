#!/usr/local/bin/python3

# @Author: hugheslou
# @Time: 2018/5/16 23:50

import calendar

monthRange = calendar.monthrange(2018, 5)
# 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数
print(monthRange)

print(calendar.mdays)
