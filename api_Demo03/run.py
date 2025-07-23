import unittest
import time
from common.handle_path import REPORT_DIR, CASE_DIR
from unittestreport import TestRunner



# 程序的入口函数
def run_test():
    suite = unittest.defaultTestLoader.discover(CASE_DIR)
    runner = TestRunner(suite,
                        filename = "report-{}.html".format(time.strftime("%Y%m%d-%H%M%S")),
                        report_dir = REPORT_DIR,
                        title = '测试报告',
                        tester = '野狐禅',
                        desc = "项目测试生成的报告")
    runner.run()

    # 将测试结果发送至邮箱
    # runner.send_email(host='smtp.qq.com',
    #                   port=465,
    #                   # 发件人邮箱
    #                   user='310046967@qq.com',
    #                   # 邮箱服务授权码，非邮箱密码
    #                   password="dvniwcfzkfwjbhjf",
    #                   # 收件人邮箱，单人字符串，多人传列表
    #                   to_addrs="310046967@qq.com",
    #                   is_file=True)

    # 拓展，自定义邮件内容和标题
    # from unittestreport.core.sendEmail import SendEmail
    # em = SendEmail(host='smtp.qq.com',
    #                port=465,
    #                # 发件人邮箱
    #                user='310046967@qq.com',
    #                # 邮箱服务授权码，非邮箱密码
    #                password="dvniwcfzkfwjbhjf")
    # em.send_email(subject="测试报告",
    #               content='XXX项目',
    #               filename='报告文件的完整路径',
    #               to_addrs='310046967@QQ.COM')

    # 钉钉推送
    # webhook = "url地址"
    # runner.dingtalk_notice(url=webhook, key="测试")

    # 企业微信推送，参考github源码



if __name__ == "__main__":
    run_test()

"""
拓展部分：
    1、测试结果的推送
        邮件发送
            开启SMTP服务
            
        推送测试结果到钉钉群
        
        推送测试结果到企业微信
        
    2.鉴权方式的补充
        RSA加密
        
        
    
"""