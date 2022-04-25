import unittest2
from lib.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # 1.找到所有需要执行的测试用例
    # 通过默认的测试用例加载器, 发现要执行的测试用例
    # 在test_case下面查找所有以Test.py结尾的测试用例
    suite = unittest2.defaultTestLoader.discover("./test_case", "*Test.py")

    # 2.执行找到的测试用例集
    # 文本的测试用例运行器执行测试用例
    # unittest2.TextTestRunner().run(suite)

    # 3.生成测试报告
    # 1.下载并复制HTMLTestRunser.py文件到我们项目
    # 指定测试报告位置
    path = "report/reportDemo.html"
    file = open(path, "wb")  # w表示写，b表示二进制方式写,description表示正文描述信息, tester测试人员名字
    HTMLTestRunner(stream=file, verbosity=1, title="电商网站自动化测试报告", description="测试环境：Chrome",tester="威廉").run(suite)




