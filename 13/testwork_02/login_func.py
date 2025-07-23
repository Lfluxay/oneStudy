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

    #  账号密码正确
    res = login_check('admin','123456')
    expected = {'code': 0, 'msg': '登录成功!'}
    # 传统方式
    # if res == expected:
    #   print("pass")
    # 引入断言方式,若有错误，则不向下执行
    assert res == expected


    # 账号错误
    res = login_check('admin01','123456')
    expected = {'code': 1, 'msg': '账号或密码不正确!'}
    if res == expected:
        print("fail")

    # 密码错误
    res = login_check('admin','123123')
    expected = {'code': 1, 'msg': '账号或密码不正确!'}
    if res == expected:
        print("fail")
