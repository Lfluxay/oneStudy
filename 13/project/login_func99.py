users = [{'user': 'fluxay', 'password': '123456'}]

def register(username, password1, password2):
    # 判断是否有参数为空
    if not all([username and password1 and password2]):
        return {'code': 0, 'msg': '所有参数不能为空'}

    # 注册功能
    for user in users: # 遍历所有账号，判断是否存在
        if username == user['user']:
            return {'code': 0, 'msg': '该账号已存在'}
    else:
        if password1 != password2:
        # 输入两次密码不一致
            return {'code': 0, 'msg': '输入两次密码不一致'}

        else:
        # 若账号不存在，密码不重复，判断账号密码长度是否在6-18位之间
            if 6 <= len(username) <= 18 and 6 <= len(password1) <= 18:
            # 注册账号
                users.append({'user': username, 'password': password2})
                return {'code': 1, 'msg': '注册成功'}
            else:
                # 账号密码长度不对，注册失败
                return {'code': 0, 'msg': '账号密码长度应在6-18位之间'}

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


if __name__ == '__mian__':
    res = register('fluxay','123456')
    print(res)
