#!/usr/local/bin/python3

# -*-coding:utf-8-*-

# @Author: hugheslou
# @Time: 2019/12/17 16:40
import numpy

pred = numpy.array([[0.3], [0.5], [0.7]])

len_pred = len(pred)
if len_pred > 2:
    pre_value = []
    for pre in pred:
        pre_value.append(pre[0])
    mean_pred = numpy.array(pre_value).reshape(len_pred, )
else:
    if len_pred == 0:
        value_pred_0 = 0
        value_pred_1 = 0
    elif len_pred == 1:
        value_pred_0 = pred[0].tolist()[0]
        value_pred_1 = 0
    else:
        value_pred_0 = pred[0].tolist()[0]
        value_pred_1 = pred[1].tolist()[0]
    mean_pred = numpy.array([value_pred_0, value_pred_1])
    mean_pred = mean_pred.reshape(2, )

print(mean_pred)
