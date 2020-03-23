# coding: utf-8

from django.http import HttpResponse,JsonResponse
from hello.models import Test,user
from django.core import serializers
import json
from django.forms.models import model_to_dict
# 数据库操作
#新增数据
def testdb(request):
    test1 = Test(name='wang')
    test1.save()
    return HttpResponse("数据库hello_test添加name成功！看去看看吧")
def add_user(request):
    test1 = user(name='wang3',password='123')
    test1.save()
    return HttpResponse("创建用户成功！")
#修改数据
def update_psw(request):
    test2=user.objects.get(name='wang')
    test2.password='123'
    test2.save()
    return HttpResponse('修改密码成功')
#删除数据
def delect_user(request):
    test3=user.objects.get(name='wang')
    test3.delete()
    return  HttpResponse('删除成功')
#查询数据
def select_name(request):
    test4=user.objects.get(id='2').name
    return HttpResponse("查询结果：%s" %test4)

def select_all(request):
    users=" "
    passwords=" "
    ret=user.objects.all()
    for i in ret:
        users +=" " + i.name
        passwords += " " + i.password
    return HttpResponse('''<p>查询user结果：%s</p>
                        <p>查询psw结果：%s</p>''' % (users, passwords))

def select_filter(request):
    r = " "
    ret=user.objects.filter(name="wang1")
    try:
        r =ret[0].password
    except:
        r ="null"
    return HttpResponse('<p>查询结果：%s</p>' %r)

def select_values(request):
    r  = " "
    ret=user.objects.all().values("name","password")
    for i in ret:
        r += str(i)
    return HttpResponse('<p>查询结果：%s</p>' %r )

def select_exclude(request):
    users=" "
    passwords=" "
    ret=user.objects.exclude(name="wang1")
    for i in ret:
        users +=" " + i.name
        passwords += " " + i.password
    return HttpResponse('''<p>查询user结果：%s</p>
                        <p>查询psw结果：%s</p>''' % (users, passwords))

#serializers转json

def get_json(request):
    data={}
    a=user.objects.all()
    data['result']=json.loads(serializers.serialize("json",a))
    return JsonResponse(data)

#model_to_dict转字典
def to_dict(request):
    ret=user.objects.all()
    json_list = []
    for i in ret:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
    return JsonResponse(json_list,safe=False)

#value转list
def to_value(request):
    data = {}
    ret = user.objects.all().values()
    data["data"]=list(ret)
    return  JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii':False})
















