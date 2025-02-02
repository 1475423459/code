import unittest
from  Website.test_case.model.function import *
from HTMLTestRunner import HTMLTestRunner
import time

report_dir = './test_report'
test_dir = './test_case'

print("start run testcase...")
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + 'result.html'

print("start write report...")
# 运行前记得把BSTestRunner.py 120行‘unicode’ 换成‘str’
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="localhost login test")
    runner.run(discover)
f.close()

print("find latest report...")
# 查找最新的测试报告
latest_report = latest_report(report_dir)
# 邮件发送报告

print("send email report...")
send_mail(latest_report)
print("test end!")