# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author: rxl


def operate_file():
    with open("title.txt", "a+", encoding='utf-8') as f:
        f.write("this is a 例子1\n")


def read_file():
    with open("title.txt", "r+", encoding='utf-8') as f:
        content = f.read()
        print(content)
        print(content.find('例子d') > -1)


if __name__ == "__main__":
    # operate_file()
    read_file()