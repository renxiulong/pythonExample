# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
author: rxl
date: 20190905
description: set集合类型的常用方法 Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算
"""


def main():
    """
    说明： Python中允许通过一些特殊的方法来为某种类型或数据结构自定义运算符（后面的章节中会讲到），
    上面的代码中我们对集合进行运算的时候可以调用集合对象的方法，也可以直接使用对应的运算符，
    例如&运算符跟intersection方法的作用就是一样的，但是使用运算符让代码更加直观
    :return:
    """
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(type(range(1, 10)))  # <class 'range'>
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    set2.update((13, 14))
    print(set1)
    print(set2)
    set2.discard(5)  # 删除该元素 如果没有此元素，什么也不做，并不报错和异常
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)
    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))


if __name__ == '__main__':
    main()