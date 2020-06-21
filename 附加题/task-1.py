#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wjhao'

def compare_number(a, b):
    """
    示例 1:
        输入: version1 = "0.1", version2 = "1.1"
        输出: -1
        示例 2:
        输入: version1 = "1.0.1", version2 = "1"
        输出: 1
        示例 3:
        输入: version1 = "7.5.2.4", version2 = "7.5.3"
        输出: -1
        示例 4：
        输入：version1 = "1.01", version2 = "1.001"
        输出：0
        解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
        示例 5：
        输入：version1 = "1.0", version2 = "1.0.0"
        输出：0
        解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。

    :return:
    """
    al = a.split('.')
    bl = b.split('.')
    if len(al) > len(bl):
        cnl = len(bl)
    else:
        cnl = len(al)
    for i in range(cnl):
        if int(al[i]) > int(bl[i]):
            return 1
        elif int(al[i]) < int(bl[i]):
            return -1

    if len(al) > len(bl):
        if sum([int(i) for i in al[len(bl):]]) > 0:
            return 1
    else:
        if sum([int(i) for i in bl[len(al):]]) > 0:
            return -1
    return 0