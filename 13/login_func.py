def login_check(username=None, password=None):
    """
    :param username: 账号
    :param password: 密码
    :return: dict type
    """
    if username != None and password != None:
        if username == 'admin' and password == '123456':
            return {'code': 0, 'msg': '登录成功!'}
        else:
            return {'code': 1, 'msg': '账号或密码不正确!'}
    else:
        return {'code': 1, 'msg': '参数不能为空!'}


if __name__ == "__main__":
    pass