import unittest
import HTMLTestRunner
import time

#指定测试用例和测试报告路径
test_dir='./test_case'
report_dir='./reports'

#加载测试用例
discover=unittest.defaultTestLoader.discover(test_dir,pattern='login_test.py')

#定义报告文件格式,report_dir+'/'保存路径
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name =report_dir+'/'+now + '_test_report.html'

#运行用例并且生成报告
with open(report_name,'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream = f, title='Login API Test Report',description="test test test")
    runner.run(discover)
