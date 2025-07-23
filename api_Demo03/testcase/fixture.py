import requests
from common.handle_conf import conf
from jsonpath import jsonpath

class BaseTest:

    @classmethod
    def admin_login(cls):

        url = conf.get("env", 'base_url') + '/member/login'
        # 管理员登录
        # 1.准备登录数据
        params = {
            "mobile_phone": conf.get("test_data", 'admin_mobile'),
            "pwd": conf.get('test_data', "admin_pwd")
        }
        headers = eval(conf.get('env', 'headers'))
        # print(headers)

        # 2.请求接口
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()
        # print(res)

        # 3.获取响应数据并提取,匹配到的是列表，通过下标取值
        admin_token = jsonpath(res, '$..token')[0]
        # print(admin_token)
        headers['Authorization'] = 'Bearer ' + admin_token
        cls.admin_headers = headers

        # 4.提取用户id,匹配到的是列表，通过下标取值
        cls.admin_member_id = jsonpath(res, '$..id')[0]
        # print(cls.member_id)

    @classmethod
    def user_login(cls):
        url = conf.get("env", 'base_url') + '/member/login'
        # 普通用户登录
        params = {
            "mobile_phone": conf.get('test_data', 'mobile'),
            "pwd": conf.get('test_data', 'pwd')
        }
        headers = eval(conf.get('env', 'headers'))
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()

        cls.token = jsonpath(res, '$..token')[0]
        headers['Authorization'] = 'Bearer ' + cls.token
        cls.headers = headers
        cls.member_id = jsonpath(res, '$..id')[0]

    @classmethod
    def add_project(cls):
        # 添加项目
        url = conf.get('env', 'base_url') + '/loan/add'
        params = {
                "member_id": cls.member_id,
                "title": "投资实现财富自由",
                "amount": 5000,
                "loan_rate": 18,
                "loan_term": 12,
                "loan_date_type": 1,
                "bidding_days": 10}

        response = requests.post(url=url, json=params, headers=cls.headers)
        res = response.json()
        # print(res)

        cls.loan_id = jsonpath(res, '$..id')[0]

    @classmethod
    # 添加项目
    def audit(cls):
        url = conf.get('env', 'base_url') + '/loan/audit'
        params = {
            "loan_id": cls.loan_id,
            "approved_or_not": True
            }
        # 发送请求，对项目进行审核
        requests.patch(url=url, json=params, headers=cls.admin_headers)
        # res = response.json()
        # print(res)
        # cls.loan_id = jsonpath(res, '$..id')[0]