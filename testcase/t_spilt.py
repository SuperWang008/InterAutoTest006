# mStr = '192.168.1.1,192.168.1.2,192.168.1.3'
# lista=mStr.split(",")
# print(lista)
# for i in lista:
#     print(i)
# for i in range(len(lista)):
#     print("序号：%s   值：%s" % (i + 1, lista[i]))
#
# a= 'longin'
# tmp1 = {
#     "aaa" : "911",
#     "bbb" : '522'
# }
# b='order'
# tmp2 = {
#     "ccc" : "666",
#     "ddd" : '222'
# }
#
# list_b = list()
# list_b.append(zip(a,tmp1))
# list_b.append(zip(b,tmp2))
# print(list_b)


# import json

# with open(r"C:\Users\Administrator\Desktop\datajson.txt", "a") as fp:
#     fp.write(json.dumps(tmp1,indent=4))

# with open(r"C:\Users\Administrator\Desktop\datajson.txt", 'r') as load_f:
#     load_dict = json.load(load_f)
#
# print(type(load_dict), load_dict)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    list = ['html', 'js', 'css', 'python']

    # 方法1
    # print '遍历列表方法1：'
    for i in list:
        print ("序号：%s   值：%s" % (list.index(i) + 1, i))

    # print '\n遍历列表方法2：'
    # 方法2
    for i in range(len(list)):
        print ("序号：%s   值：%s" % (i + 1, list[i]))

    # 方法3
    # print '\n遍历列表方法3：'
    for i, val in enumerate(list):
        print ("序号：%s   值：%s" % (i + 1, val))

    # 方法3
    # print '\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：'
    for i, val in enumerate(list, 2):
        print ("序号：%s   值：%s" % (i + 1, val))



