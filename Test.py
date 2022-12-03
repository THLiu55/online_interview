# coding:utf-8
import unittest
from blueprints import user
from blueprints.user import user_bp
#importrints.user
import json
from app import app
from HTMLTestRunner import HTMLTestRunner
import os



class TestLogin(unittest.TestCase):
    """定义测试案例"""

    # 测试代码执行之前调用 (方法名固定)
    def setUp(self):
        """在执行具体的测试方法前，先被调用"""
        # 可以使用python的http标准客户端进行测试
        # urllib  urllib2  requests
        # app.config['TESTING'] = True  # 指定app在测试模式下运行
        app.testing = True  # 指定app在测试模式下运行。 (测试模式下,视图中的意外异常可以正常打印显示出来)
        # 使用flask提供的测试客户端进行测试 (Flask客户端可以模拟发送请求)
        self.client = app.test_client()

    # 测试代码。 (方法名必须以"test_"开头)
    def test_login(self):
        """测试用户登录"""
        # 使用Flask客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        response = self.client.post("/login", follow_redirects=True,data={"user":"1523073873@qq.com","pass":"123456"})
        # respoonse.data是响应体数据
        resp_json = response.data
        resp_text = response.get_data(as_text=True)
        code=response.status_code

        self.assertEqual(code,200)
        self.assertIn("Schedule for interview",resp_text)

    def XXXtest_logout(self):
        """测试模拟场景，用户名或密码正确测试"""
        response = self.client.post("/login", follow_redirects=True,data={"user":"1523073873@qq.com","pass":"123456"})
        # 使用Flask客户端向后端发送get请求
        #user.login()
        #user.logout()
        headers1 = response.headers
        print("aaa")
        #print(headers1)
        #print(response.get_data("cookie"))
        #print('bbb')
        #self.client.set_cookie('localhost', 'session', response.request.cookies)
        response = self.client.get("/logout")
        # respoonse.data是响应体数据
        resp_json = response.data
        resp_text = response.get_data(as_text=True)
        code=response.status_code

        #print(resp_text)

        #self.assertEqual(code,200)
        #self.assertIn("Schedule for interview",resp_text)


    # 测试代码。 (方法名必须以"test_"开头)
    def test_login_nagetive(self):
        """反向测试-用户登录"""
        response = self.client.post("/login", follow_redirects=True,
                                    data={"user": "15@qq.com", "pass": "123456"})
        resp_json = response.data
        resp_text = response.get_data(as_text=True)
        code = response.status_code

        self.assertEqual(code, 200)
        self.assertIn("/login", resp_text)





    def test_register_check(self):
        """测试注册是否成功"""
        # 使用Flask客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        header={'Content-Type': 'application/json;charset=UTF-8'}
        data = {"email": "1523073873@qq.com", "userName": "liwx", "password": "123456", "captcha": "WBuTZQ"}
        response = self.client.post("/register", follow_redirects=True, json= data, headers=header)
        # respoonse.data是响应体数据
        resp_json = response.data
        resp_text = response.get_data(as_text=True)
        code=response.status_code
        #print(resp_text)
        #print("abc" + str(code))

        self.assertEqual(code,200)
        self.assertIn("invalidSignUpEmail",resp_text)



    def test_my_mail(self):
        """邮箱正确性测试"""
        # 使用Flask客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        header={'Content-Type': 'application/json;charset=UTF-8'}
        data = {"email": "a7@qq.com"}
        response = self.client.post("/captcha", follow_redirects=True, json=data, headers=header)
        # respoonse.data是响应体数据
        resp_json = response.data
        resp_text = response.get_data(as_text=True)
        code=response.status_code
        #print(resp_text)
        #print("abc" + str(code))

        self.assertEqual(code,200)
        #self.assertIn("invalidSignUpEmail",resp_text)

    def test_password_check(self):
        """测试密码是否正确"""
        # 使用Flask客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        header={'Content-Type': 'application/json;charset=UTF-8'}
        #data = {"the_email": "1523073873@qq.com"}
        #the_email = "1523073873@qq.com"
        data = {"email": "1523073873@qq.com"}
        response = self.client.post("/forget_form_password", follow_redirects=True, json=data, headers=header)
        # respoonse.data是响应体数据
        resp_json = response.data
        resp_text = response.get_data(as_text=True)
        code=response.status_code
        #print(resp_text)
        print("test password_check status_code " + str(code))

        self.assertEqual(code,200)
        #self.assertIn("invalidSignUpEmail",resp_text)

    def test_finish(self):
        """测试结束房间"""
        #code = request.form.get("code")
        #room_id = request.form.get("id")
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        form={"code":"1111","id":10}

        response =self.client.post("/finish",data = form)
        resp_json = response.data
        resp_text = response.get_data(as_text=True)
        code = response.status_code
        print(resp_text)
        code = response.status_code
        print(code)
        self.assertEqual(code,200)
        #self.assertIn("total_interview",resp_dict)

    def test_schedule_total_interview(self):
        """测试返回总的面试场次"""
        response =self.client.get("/schedule/total_interview")
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        resp_text = response.get_data(as_text=True)
        code = response.status_code
        #print(resp_text)
        code = response.status_code
        #print(code)
        self.assertIn("total_interview",resp_dict)

    def test_schedule_per_interview(self):
        """测试面试安排"""
        response = self.client.get("/schedule/per_interview")
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        resp_text = response.get_data(as_text=True)
        code = response.status_code
        #print(resp_text)
        #print(code)
        self.assertEqual(code,200)
        self.assertIn("data", resp_dict)




    def xxtestxx_template(self):
        # response.get_data(as_text=True)
        response = self.client.get("/jump/login.html")
        # respoonse.data是响应体数据
        resp_json = response.data
        resp_text = response.get_data(as_text=True)
        code = response.status_code
        # 按照jsoresponse.status_coden解析
        # resp_dict = json.loads(resp_json)
        # print(resp_json)
        #print("retcode=" + str(code))
        #print(response.history)
        #print(resp_text)
        #print(response.request)
        self.assertEqual(code, 200)
        # 使用断言进行验证
        # self.assertIn("code", resp_dict)
        # code = resp_dict.get("code")
        # self.assertEqual(code, 2)

        # 使用断言进行验证
        # self.assertIn("code", resp_dict)
        # code = resp_dict.get("code")
        # self.assertEqual(code, 1)
        # 测试只传name
        # response = self.client.post("/dologin", data={"name": "admin"})
        # respoonse.data是响应体数据
        #  resp_json = response.data
        # 按照json解析
        # resp_dict = json.loads(resp_json)
        # 使用断言进行验证
        #  self.assertIn("code", resp_dict)
        #  code = resp_dict.get("code")
        #  self.assertEqual(code, 1)



if __name__ == '__main__':
    #unittest.main()  # 进行测试
    print(os.getcwd())
    reportPath = os.getcwd() + "\\report\\report.html"
    #suit =unittest.TestSuite()
    #suit.addTest(TestLogin("test_wrong_name_password"))

    test_dir = './'  # 当前路径
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py')  # iot_*.py表示iot_开头的所有测试用例
    # reportPath = os.getcwd() + "report\\report.html"
    filename = os.getcwd() + "\\report\\report.html"
    # suit = unittest.TestSuite()
    # suit.addTest(TestLogin("test_wrong_name_password"))
    f = open(filename, "w", encoding="utf-8")

    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="Online interview logon test report", description="my description")
    runner.run(discover)
    f.close()

    print("The report is on " + filename)



