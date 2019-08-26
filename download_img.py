# -*- coding: utf-8 -*-
import requests


def download_image():
    url = 'http://upload.hzau.edu.cn/2019/0824/1566658808569.jpg'
    response = requests.get(url)
    with open('1.jpg', 'wb') as f:
        f.write(response.content)


if __name__ == "__main__":
    download_image()