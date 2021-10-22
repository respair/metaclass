from newlist import NewList
from metaclass import *

if __name__ == "__main__":
    cc = CustomClass()
    print(cc.custom_x)
    print(cc.custom_line())
    a = [1, 2, 3, 4, 5, 6, 7]
    b = [4, 2, 9, 0, -5, -10, 7, 12, 2]
    l1 = NewList(a)
    l2 = NewList(b)
    print((b - l1).list)
    print((l1 - b).list)
    print((l1 - l2).list)
    print(l1.list)
    print(l2.list)
    print((l1 + b).list)
    print((l1 + l2).list)
    print((b + l1).list)
    print(l1 > l2)
    print(l1 < l2)
    print(l1 == l2)
