from selenium import webdriver
import unittest2
import time


class LoginTest(unittest2.TestCase):
    def test_login(self):
        self.driver.get("http://127.0.0.1/index.php?m=user&c=public&a=login")
        self.driver.find_element_by_id('username').send_keys("william")
        self.driver.find_element_by_id('password').send_keys("123456")
        self.driver.find_element_by_css_selector(".login_btn.fl").click()
        time.sleep(3)
        # 页面定位
        print(self.driver.title)
        print(self.driver.current_url)
        # 元素定位
        welcome = self.driver.find_element_by_css_selector("div.site-nav-right.fr > a:nth-child(1)").text
        print(welcome)

        # 运行当前脚本输出  我的会员中心 - 道e坊商城 - Powered by Haidao，您好 william
        search = self.driver.find_element_by_css_selector('.btn1').get_attribute('value')
        print(search)
        # 用断言代替if else语句做判断
        # 断言成功或者失败会写到测试报告上
        self.assertEqual("我的会员中心 - 道e坊商城 - Powered by Haidao",self.driver.title)
        self.assertEqual("http://127.0.0.1/index.php?m=user&c=index&a=index", self.driver.current_url)
        self.assertEqual("您好 william", welcome)
        # self.assertEqual("搜    索", search) #\xa0\xa0\xa0\xa0
        self.assertEqual("搜 索", search)   # 这里故意改错

    @classmethod
    def setUpClass(cls):
        # 打开浏览器, 做预处理工作
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

