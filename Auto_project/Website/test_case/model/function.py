from  selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#截图方法
def inser_img(driver,filename):

    #获取当前模块所在路径
    func_path=os.path.dirname(__file__)
    # print("func_path is %s" %func_path)

    #获取test_case目录
    base_dir=os.path.dirname(func_path)
    # print("base_dir is %s" %base_dir)

    #将路径转化为字符串
    base_dir=str(base_dir)

    #对路径的字符串进行替换
    base_dir=base_dir.replace('\\','/')
    # print(base_dir)

    #获取项目文件的根目录路径
    base=base_dir.split('/Website')[0]
    # print(base)

    #指定截图存放路径
    filepath=base+'/Website/test_report/screenshot/'+filename
    # print(filepath)
    driver.get_screenshot_as_file(filepath)

#查找最新的测试报告
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    # print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file

#将测试报告发送到邮件
def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = 'wjuan2019@163.com'
    password = 'XTCOEWUDIECQUSFE'   #在开启POP3/SMTP服务，并开启客户端授权密码时会设置授权码

    sender = 'wjuan2019@163.com'
    receives = ['1475423459@qq.com']

    subject = 'Web Selenium 自动化测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")


#if __name__ == '__main__':
    #driver=webdriver.Firefox()
    #driver.get("http://www.sogou.com")
    #inser_img(driver,"sogou.png")
    #driver.quit()
    #latest_report = latest_report('/Website/test_report')
    #send_mail(latest_report)