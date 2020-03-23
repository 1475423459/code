import keyword
#my test
from test.mod_generics_cache import B
import cmath
'''
my test
my test
user_name = 'juan wang'
user_age = '25'
print("用户名:",user_name,"年龄:",user_age,sep='|',end=' ')
print(user_name)
user_name = 'xiao wang'
print(user_name)
print(type(user_name))

f = open('C:\\Users\\wangjuan\\Desktop\\test1.txt','w')
print("写入到文件",file = f)
f.close()

a = 34
print(a)
a = 999999999999999
print(a)
print(type(a))

hex_value1=0b10111
print(hex_value1)

af1 = 2.343434
print("af1的值：",af1,"af1的类型：",type(af1))

af2 = 5.12e2
print("af2的值：",af2,"af2的类型：",type(af2))
ac1 = 3 + 0.2j
print(ac1)
print(type())


str1 = '"we\'are yung women",says the younth'
print(str1)
str2 = 'hehhehe'
print(str2)
s = str1 + str2
print(s)
s1 = '呜呜呜呜'
n = 100
print(s1 + str(n))
print(s1 + repr(n))
print(s1)
print(repr(s1))
msg = input("请输入你的值： ")
print(type(msg))
print(msg)

s1 = 

a = 5
b = 3
st = "a大于b" if a>b else "a小于b"
print(st)

a_tuple = ('a','b','c','1','2','3')
print(a_tuple[-1])
print(a_tuple[1:6:3])
b_tuple = ('4','5','6')
c_tuple = a_tuple + b_tuple
print(c_tuple)

order_endings = ('st','nd','rd')\
    + ('th',)*17 + ('st','nd','rd')\
    + ('th',)*7 + ('st',)
print(order_endings)
day = input("输入日期（1-31）： ")
day_int = int(day)
print(day + order_endings[day_int - 1])

a_tuple = ('a','b','c','1','2','3')
print(max(a_tuple))
print(min(a_tuple))
print(len(a_tuple))
a_list=list(a_tuple)
print(a_list)
a_range = range(1,3)
b_list=list(a_range)
print(a_range)
print(b_list)
b_list.append('1')
print(b_list)
b_list.append(['1','2'])
print(b_list)
b_list.extend(['w','d'])
print(b_list)
del b_list[1]
print(b_list)

name = ['wj','1','2']
print(name)
name[1] = '2'
print(name)

b_list = list(range(1,5))
print(b_list)
print(b_list.count(2))
print(b_list.index(2))
print(b_list.reverse())
print(b_list)

print(dict())
vegetable = [('w',1.1),('x',1.2),('y',1.3)]
dict1 = dict(vegetable)
print(dict1)
print(dict1['w'])
dict1['x'] = 3.4
dict1['z'] = 4.5
print(dict1)
del dict1['w']
print(dict1)
print('w' in dict1)
print('x' in dict1)
print(dict1.get('x'))
i = dict1.items()
print(list(i))
j = dict1.keys()
print(list(j))
k = dict1.values()
print(list(k))
print(dict1.pop('x'))
print(dict1)
print(dict1.popitem())
print(dict1)
dict2 = dict1.fromkeys(['a','y'])
print(dict2)

s_age = input("请输入您的年龄： ")
age = int(s_age)
if age > 18 :
    print("年龄大于18岁，已成年！！！")
else:
    print("年龄小于18岁，未成年，还是个宝宝！！！")


s = ""
if s :
    print('s不是空字符串')
else:
    print('s是空字符串')
a_list = []
if a_list:
    print('a_list不是空列表')
else:
    print('a_list是空列表')
a_dict = {}
if a_dict :
    print('a_dict不是空字典')
else:
    print('a_dicr是空字典')

age = 45
if age > 60 :
    print("老年人")
elif age > 40 :
    pass
elif age > 20 :
    print("年青人")
    
s_age = input("请输入您的年龄： ")
age = int(s_age)
assert 20 < age < 80
print("您的年龄在20-80岁之间")

count_i = 0
while count_i < 10 :
    print("count:",count_i)
    count_i += 1
print("循环结束")

a_tuple = ('1', 'srew', 'ewrwer')
i = 0
while i < len(a_tuple):
    print(a_tuple[i])
    i += 1

#while遍历
scr_list = [1, 3, 4 ,7, 10, 13,14]
a_list = []
b_list = []
c_list = []
while len(scr_list) > 0 :
    ele = scr_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else :
        c_list.append(ele)
print("整除3：",a_list)
print("除以3余数1：",b_list)
print("除以2余数2：",c_list)
#计算阶乘
s_max = input("请录入想要计算的阶乘：")
max = int(s_max)
result = 1
#注意此处开始遍历
for num in range(1, max + 1):
    result *= num
print(result)

#遍历元组
a_tuple = ('my', 'you', 'our', 'us')
for ele in a_tuple:
    print("当前元素：",ele)

#遍历计算列表中的值
src_list = [12, 45, 3.4, 13, 'a', 4, 56, 'crezyit', 109.5]
my_sum = 0
my_count = 0
for ele in src_list:
    if isinstance(ele,int) or isinstance(ele,float):
        print(ele)
        my_sum += ele
        my_count += 1
print("总和：",my_sum)
print("平均值：",my_sum/my_count)

#for-in遍历字典
my_dict = {'语文': 89, '数学': 67, '英文': 90}
for key,value in my_dict.items():
    print('key:',key)
    print('value:',value)
for key in my_dict.keys():
    print('key:',key)
for value in my_dict.values():
    print('value:',value)


#把列表中出现的次数列为字典中的key,value
src_list = [12, 45, 3.4, 12, 'flick', 45, 3.4, 'flick', 45, 3.4]
statistics = {}
for ele in src_list:
    if ele in statistics:
        statistics[ele] += 1
    else:
        statistics[ele] = 1
for ele,count in statistics.items():
    print("%s出现的次数未：%d" % (ele,count))


a_range = range(10)
a_list = [x*x for x in a_range if x % 2 == 0]
print(a_list)

d_dict=[(x,y) for x in range(5) for y in range(4)]
print(d_dict)

#zip()函数用法
a = ['a', 'b', 'c']
b = [1, 2,3]
c = [x for x in zip(a,b)]
print(c)

#反序reversed()
a = range(10)
b = [x for x in reversed(a)]
print(b)

b = ['a', 'ab', 'abc', 'ancd']
c = sorted(b, key = len)
print(c)

#break 跳出循环体
for i in range(0,10):
    print("i的值：",i)
    if i == 2:
        break
    else:
        print("else块：",i)


exit_flag = False
for i in range(0,5):
    for j in range(0,3) :
        print("i的值为： %d,j的值为：%d" % (i,j))
        if j == 1:
            exit_flag = True
            break
        if exit_flag :
            break
#:return跳出循环            
def test():
    for i in range(0,3):
        print("I的值是： ",i)
        if i == 1:
            return
        print("return后的输出语句")

test()
#函数
def my_max(x,y):
    z = x if x >y else y
    return z
def say_hi(name):
    print("===正在执行say_hi函数===")
    return  name + ",您好！"
a = 5
b =9
result =  my_max(a,b)
print("结果：",result)
print(say_hi("卷卷"))

help(my_max)
print(my_max.__doc__)

#5.1.4返回多个值的函数
def sum_and_avg(list):
    sum = 0
    count = 0
    for e in  list:
        if isinstance(e,int) or isinstance(e,float):
            count += 1
            sum += e
    return sum,sum/count
my_list = [1,2,34,'e',4.5]
tp = sum_and_avg(my_list)
print(tp)

#5.1.5 递归函数
def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return  2 * fn(n-1) + fn(n-2)
print("jieguo",fn(5))


#5.2.2形参默认值
def print_truangle(char, height = 5):
    for i in range(1,height+1):
        for j in range(height-i):
            print(' ',end = '')
        for j in range(2*i -1):
            print(char,end='')
        print()
print_truangle('@',7)

#5.2.3参数手记（个数可变的参数）
def test(* books, a):
    print(books)
    for b in books:
        print(b)
    print(a)
#调用test()函数
test( "语文", "数学", "英文", a = 10)

#逆向参数收集-元组/列表
def foo(name, *nums):
    print("name参数： ", name)
    print("num参数: ", nums)
my_tuple = (1, 2, 3)
#将my_tuple元素传入nums参数
foo('fkit', *my_tuple)
foo(*my_tuple)
foo(my_tuple)
#逆向参数收集-字典
def bar(book, price, desc):
    print(book, "这本书的价格是：", price)
    print('描述信息', desc)
my_dict = {'price': 89, 'book': '疯狂python', 'desc': '这是一本初级入门图书'}
bar(**my_dict)

#5.2.5函数的参数传递机制
#用“=”赋值
def swap(a, b):
    a, b = b, a
    print("在swap函数，a的值是：",a ,"变量b的值是：",b)
a = 6
b = 9
swap(a, b)
print("交换结束的值a:",a , "交换结束的值b:",b)
#数据包装成列表字典等可变对象，对其赋值
def swap(dw):
    dw['a'], dw['b'] = dw['b'], dw['a']
    print("dw[a]的值：", dw['a'], "dw[b]的值：", dw['b'])
dw = {'a' : 6, 'b' : 7}
swap(dw)
print("交换后的值dw[a]:",dw['a'] ,"交换后的值dw[b]:",dw['b'])
#局部函数
def get_math_func(type, nn):
    def square(n):
        return n * n
    def cube(n):
        return n * n * n
    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
            return result
    if type == "square":
        return square(nn)
    elif type == "cube":
        return cube(nn)
    else:
        return factorial(nn)
print(get_math_func("square", 3))
print(get_math_func("cube", 3))
print(get_math_func("", 3))

#5.4.1函数赋值给变量
def pow(base,exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result
my_fun = pow
print(my_fun(3,4))

#用函数作为函数形参
def map(data, fn):
    result = []
    #遍历数组中的元素
    for e in data:
        result.append(fn(e))
    return  result
#定义一个计算平方的函数
def square(n):
    return n * n
#定义一个计算立方的函数
def cube(n):
    return n * n * n
data = [3, 4, 9, 5, 8]
print("原数据：", data)
print(map(data,square))
print(map(data,cube))

#局部函数
def get_math_func(type):
    #定义一个计算平方的局部函数
   def square(n):
       return n * n
   def factorial(n):
       result = 1
       for index in range(2, n + 1):
           result *= index
       return result
   if type == "square":
       return square
   else:
       return factorial
math_func = get_math_func("square")
print(math_func(5))

#lambda局部函数
def get_math_func(type):
    result  = 1
    if type == 'square':
        return lambda n: n * n
    else:
        return lambda n: n * n * n
math_func = get_math_func("cube")
print(math_func(5))


#定义一个函数，该函数可接收一个 list 作为参数，该函数使用直接选择排序对 list 排序

def a_list(data):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_  index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    print("排序后：", data)
a = [1,2,5,3,9,1]
a_list(a)


# 定义立方和的函数
def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i*i*i

    return sum


# 调用函数

print(sumOfSeries(5))

#简单类
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self):
        print("%s 会唱歌" % self.name)
    def dance(self):
        print("年龄 %d 的 %s 会跳舞" % (self.age, self.name))

P = Person("WANG", 15)
print(P.name)
print(P.age)
P.dance()
P.sing()
P.skills = ['heiehi']
print(P.skills)


def foo():
    print("全局空间的foo方法")
bar = 20
class Bird:
    def foo(self):
        print("Bird空间的foo方法")
    bar = 200
foo()
print(bar)
o =  Bird()
o.foo()
print(Bird.bar)

#类方法示例
class Tool(object):
    count = 0
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)
    def __init__(self, name):
        self.name = name
        Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("锄头")
Tool.show_tool_count()

#静态方法
class Dog(object):
    def run(self):
        print("跑啊,,,,,,,")


#***--***单例设计
class MusicPlayer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        #判断类属性是否空对象
        if cls.instance is None:
           #若对象为创建，调用父类方法，未对象分配空间
           cls.instance = super().__new__(cls)
        #返回类属性保存对象引用
        return cls.instance
    def __init__(self):
        print("初始化")
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)

#**--**单例设计，只执行一次__init__

class MusicPlayer(object):
    instance = None
    init_flg = False
    def __new__(cls, *args, **kwargs):
        #判断类属性是否空对象
        if cls.instance is None:
            #若对象为创建，调用父类方法，未对象分配空间
            cls.instance = super().__new__(cls)
        #返回类属性保存对象引用
        return cls.instance
    def __init__(self):
        #判断是否执行
        if MusicPlayer.init_flg:
            return
        #未执行则继续执行
        print("初始化")
        #修改属性标记
        MusicPlayer.init_flg = True
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)

try:
    #不能确定正确执行的代码
    num = int(input("请输入整数： "))
except:
    #错误的处理代码
    print("请输入正确的整数")
print("--")

#抛出异常完整流程
try:
    num = int(input("输入一个整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误%s" % result)
else:
    print("尝试成功")
finally:
    print("无论成功与否都会执行代码")

#异常传递性
def demo1():
    return int(input("输入整数："))
def demo2():
    return demo1()
try:
    print(demo1())
except Exception as result:
    print("错误信息%s" % result)


#主动抛出raise异常
def input_password():
    #1.提示用户输入密码
    pwd = input("请输入密码：")
    #2.判断密码长度
    if len(pwd) > 8:
        return pwd
    #3.若长度小于8，抛出异常
    print("主动抛出异常")
    ex = Exception("密码长度不够")
    raise ex
try:
    print(input_password())
except Exception as result:
    print(result)

#import 导入模块
import test1 as Test
import test2
Test.say_hello()
test2.say_hello()
dog = Test.Dog()
print(dog)
cat = test2.Cat()
print(cat)

#导入模块部分功能
from test1 import Dog
from test2 import say_hello

say_hello()
wangcai = Dog()
print(wangcai)


#不同模块导入同名函数
from test1 import say_hello as say_hello1
from test2 import say_hello
say_hello()
say_hello1()


#导入顺序
import random
print(random.__file__)
rand = random.randint(1,10)
print(rand)

#导入包
import he_message
he_message.send_message.send("你好呀")
he_message.recive_message.recive()


#文件操作
#1.打开文件
file = open("11.txt","w")
#2.读取文件
file.write("hello")
#3.关闭文件

file.close()


#读取文件内容-行
file = open("11.txt")
while True:
    text =  file.readline()
    if not text:
        break
    print(text)
file.close()


#复制小文件
file_read = open("11.txt")
file_write = open("11[复制文件].txt","w")
text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()


#复制大文件
file_read = open("11.txt")
file_write = open("11[复制文件].txt","w")
while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()
'''

#eval 函数

str = input("请输入计算：")
print(eval(str))





















































































































































