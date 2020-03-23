import requests
#1.发送get请求
#r=requests.get(base_url+'/get')
#print(r.status_code)
#2.发送post请求
#r=requests.post(base_url+'/post')
#print(r.status_code)
#3.发送PUT请求
#r=requests.put(base_url+'/put')
#print(r.status_code)
#4.发送Delete请求
#r=requests.delete(base_url+'/delete')
#print(r.status_code)

#1-1url参数传递

#param_data={'user':'zxw','pasword':'999'}
#r=requests.get(base_url+'/get',params=param_data)
#print(r.url)
#print(r.status_code)

#2.设置header
#form_data={'user':'zxw','pasword':'999'}
#header={'user-agent':'Mozilla/5.0'}
#r=requests.post(base_url+'/post',data=form_data,headers=header)
#print(r.text)
#print(r.json())


#设置cookie
#cookie={'user':'www'}
#r=requests.get(base_url+'/cookies',cookies=cookie,timeout=0.001)
#print(r.text)


#获取cookie值
#r=requests.get('http://www.baidu.com')
#print(type(r.cookies))
#for key,value in r.cookies.items():
  #  print(key+':'+value)

#上传文件

#form_data={'user':'www'}
#file={'file':open('11.txt','rb')}
#r=requests.post(base_url+'/post',data=form_data,files=file)
#print(r.text)



#生成会话对象
#s=requests.Session()
#base_url = 'http://httpbin.org'
#r=s.get(base_url+'/cookies/set/user/123')
#print(r.text)

#r=s.get(base_url+'/cookies')
#print(r.text)

#r=requests.get('https://www.12306.cn/')
#print(r.text)

from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
base_url = 'http://httpbin.org'
#身份认证-BasicAuth
r=requests.get(base_url+'/basic-auth/51zxw/8888',auth=HTTPBasicAuth('51zxw','8888'))
print(r.text)

#身份认证——DigestAuth
r=requests.get(base_url+'/digest-auth/auth/zxw/6666',auth=HTTPDigestAuth('zxw','6666'))
print(r.text)