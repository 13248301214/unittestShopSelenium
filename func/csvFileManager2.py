import csv
import os


def reader(filename):
    list = []
    # path = "../test_data/" + filename
    base_path = os.path.dirname(__file__)
    path = base_path.replace("func", "test_data/" + filename)
    # 如果打开很多csv,会占用很多内存资源，所以要关闭
    # file = open(path)
    with open(path) as file:
        table = csv.reader(file)
        # 删除第一行标题
        i = 0
        for row in table:
            if i == 0:
                pass
            else:
                list.append(row)
            i = i + 1
    return list

# 调用函数
print(reader("register_test_cases.csv"))



