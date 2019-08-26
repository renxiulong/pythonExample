import os


def init():
    file = os.open("d:\point.html", os.O_RDONLY)
    print(os.read(file, 4096).decode("utf-8"))


print('end', __name__)
if __name__ == '__main__':
    print('end')
    init()