# coding=utf-8
from distutils.core import setup
setup(name="he_message",  # 包名
      version="1.0",  # 版本
      description="wjuan's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="wjuan",  # 作者
      author_email="wjuan2019@163.com",  # 作者邮箱
      url="www.baidu.com",  # 主页
      py_modules=["he_message.send_message",
                  "he_message.recive_message"])