# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
author: rxl
date: 20190905
description: tuple元组类型的常用方法
"""
import sys


def main():
    """
    Python 的元组与列表类似，不同之处在于元组的元素不能修改，在前面的代码中我们已经不止一次使用过元组了。顾名思义，我们把多个元素组合到一起就形成了一个元组，所以它和列表一样可以保存多条数据
    :return:
    """
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'  # TypeError
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)
    # 将元组转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(type(fruits_tuple))
    print(type(fruits_list))
    print(sys.getsizeof(fruits_tuple))  # 元组占用存储数据的空间
    print(sys.getsizeof(fruits_list))  # 相同元素的列表占用存储数据的空间


if __name__ == "__main__":
    main()