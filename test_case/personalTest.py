from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_case.BaseTestCase import BaseTestCase
import time


class PersonalTest(BaseTestCase):
    def test_personal(self):
        # 登录接口
        self.driver.get("http://127.0.0.1/index.php?m=user&c=public&a=login")
        self.driver.find_element_by_id('username').send_keys('william')
        self.driver.find_element_by_id('password').send_keys('123456')
        # 点击登录
        # driver.find_element_by_class_name('login_btn').click()
        # submit方法: 类似于click, 只能用于form表单中
        # 这里submit方法就代替了, 定位登录按钮并点击操作
        self.driver.find_element_by_id('password').submit()

        # 点击"账号设置"
        self.driver.find_element_by_link_text('账号设置').click()

        # 点击"个人资料"
        self.driver.find_element_by_partial_link_text('人资').click()

        # 修改"真实姓名"
        self.driver.find_element_by_id('true_name').clear()
        self.driver.find_element_by_id('true_name').send_keys('姚老师')

        # 选择"性别"
        # 通过css_selector的方式, 可以采用任意属性定位元素
        self.driver.find_element_by_css_selector("[value='1']").click()
        # 输入"生日"
        # 先删除readonly属性
        script = 'document.getElementById("date").removeAttribute("readonly")'
        self.driver.execute_script(script)
        # 在生日输入框中输入生日
        # 先清除
        self.driver.find_element_by_id('date').clear()
        self.driver.find_element_by_id('date').send_keys("1989-02-15")

        # 输入"QQ"
        self.driver.find_element_by_id('qq').clear()
        self.driver.find_element_by_id('qq').send_keys('88888888')

        # 点击"确定"
        # driver.find_element_by_class_name('btn4').click()
        self.driver.find_element_by_css_selector('[value="确认"]').click()

        # 弹出框处理  【处理弹出框时, 隐式等待不起作用】
        # time.sleep(3)
        # 改成显示等待  设置为每隔0.5秒检查一次,如果弹出框出来了,就执行下面代码
        # until 期望的条件是,弹出框是存在的
        # 直到满足括号中条件,才会执行后面代码
        WebDriverWait(self.driver, 30, 0.5).until(expected_conditions.alert_is_present())

        # 获取修改后的状态
        update_status = self.driver.switch_to.alert.text
        print(update_status)

        # 弹出框的确定按钮
        self.driver.switch_to.alert.accept()





