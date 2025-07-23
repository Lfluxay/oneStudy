# import re
#
# def replace_data(data, cls):
#         """
#         替换数据的方法
#         :param data: 要进行替换的字符串
#         :param cls: 测试类
#         :return:
#         """
#         while re.search('#(.+?)#', data):
#             res = re.search('#(.+?)#', data)
#             item = res.group()
#             attr = res.group(1)
#             value = getattr(cls, attr)
#             data = data.replace(item, str(value))
#         return data

# if __name__ == '__main__':
#         data = replace_data(params, DateSearch)
#         print(data)

# ==========+升级，替换数据同时可以去找测试类和配置文件中的数据++++++++++++++++++++++++++++++++++++++
import re
from common.handle_conf import conf

def replace_data(data, cls):
        """
        替换数据的方法
        :param data: 要进行替换的字符串
        :param cls: 测试类
        :return:
        """
        while re.search('#(.+?)#', data):
            res = re.search('#(.+?)#', data)
            item = res.group()
            attr = res.group(1)
            try:
                value = getattr(cls, attr)
            except AttributeError:
                value = conf.get('test_data', attr)
            data = data.replace(item, str(value))
        return data