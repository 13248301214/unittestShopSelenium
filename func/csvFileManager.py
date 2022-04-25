import csv


# 指定csv文件所在的路径
path = r"D:\pycharm_project\SeleniumTest2\test_data\register_test_cases.csv"

# 打开csv文件
file = open(path)

# 读取csv文件中的内容
table = csv.reader(file)

# 打印csv文件中的内容
for row in table:
    print(row)
