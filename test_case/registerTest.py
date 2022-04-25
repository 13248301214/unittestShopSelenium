# import ddt
from ddt import ddt, data
import unittest2
from func.csvFileManager2 import reader
from test_case.BaseTestCase import BaseTestCase


# 表示这是一个数据驱动测试类, 好处：当其中某个测试用例执行失败, 后续的测试数据继续执行, 其他测试用例不会受到影响
# @ddt.ddt
@ddt
class Register3Test(BaseTestCase):

    # 读取csv数据
    row = reader("register_test_cases.csv")

    # 表示这个方法使用数据驱动里面的数据测试
    # 表示把5行数据拆成5个变量，ddt作用相当于把for循环写在了方法外面
    # @ddt.data(*table)
    @data(*row)
    def test_register(self, row):  # 每次循环一行数据传递进来
        self.driver.get("http://127.0.0.1/index.php?m=user&c=public&a=reg")
        self.driver.find_element_by_name("username").send_keys(row[0])
        self.driver.find_element_by_name("password").send_keys(row[1])
        self.driver.find_element_by_name("userpassword2").send_keys(row[2])
        self.driver.find_element_by_name("mobile_phone").send_keys(row[3])
        self.driver.find_element_by_name("email").send_keys(row[4])
        print(self.row)  # 不加星号, 表示一个变量, 就是列表本身
        print('*' * 50)
        print(*self.row) # 添加星号, 表示4个变量, 把列表中每个元素看成单独的变量

if __name__ == '__main__':
    unittest2.main()