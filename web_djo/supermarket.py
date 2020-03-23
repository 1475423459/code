#定义仓库
repository = dict()
#定义购物清单对象
shop_list = []
#定义函数初始化商品
def init_repository():
    #初始化商品，元组代表一个商品
    goods1 = ("1000001", "语文书", 23)
    goods2 = ("1000002", "数学书", 33)
    goods3 = ("1000003", "英语书", 43)
    goods4 = ("1000004", "物理书", 53)
    goods5 = ("1000005", "化学书", 63)
    goods6 = ("1000006", "历史书", 73)
    #商品入口（放入dict中）,条码未key
    repository[goods1[0]] = goods1
    repository[goods2[0]] = goods2
    repository[goods3[0]] = goods3
    repository[goods4[0]] = goods4
    repository[goods5[0]] = goods5
    repository[goods6[0]] = goods6
#显示超市商品清单，变量代表仓库的dict字典
def show_goods():
    print("欢迎光临 卷卷个人超市")
    print("超市商品清单： ")
    print("%13s%40s%10s" % ("条码", "商品名称", "单价"))
    #遍仓库中所有values显示商品清单
    for goods in repository.values():
        print("%13s%40s%10s" % goods)
#显示购物清单，遍历代表购物清单的list列表
def show_list():
    print("=" * 100)
    #如果清单不为空，输出
    if not shop_list:
        print("还未购买商品")
    else :
        title = "%-5s | %15s |%40s |%10s |%4s |%10s" % \
                ("ID", "条码", "商品名称", "单价", "数量", "小计")
        print(title)
        print("-" * 100)
        #记录总计价钱
        sum = 0
        for i, item in enumerate(shop_list):
            id = i + 1
            code = item[0]
            name = repository[code][1]
            price= repository[code][2]
            number = item[1]
            amount = price * number
            sum = sum + amount
            line = "%-5s | %15s |%40s |%10s |%4s |%10s" % \
                   (id, code,name, price, number, amount)
            print(line)
            print("-" *100)
            print("                总计：" ,sum)
        print("=" * 100)
def add():
    code = input("请输入商品条码：\n")
    if code not in repository:
        print("条形码不存在，请重新输入")
        return
    goods = repository[code]
    number = input("请输入购买数量：\n")
    shop_list.append([code,int(number)])
def edit():
    id = input("请输入要修改的购物明细ID:\n")
    index = int(id) - 1
    item = shop_list[index]
    number = input("请输入新购买的数量：\n")
    item[1] = int(number)
def delete():
    id = input("请输入删除的明细ID:\n")
    index = int(id) - 1
    del shop_list[index]
def payment():
    show_list()
    print("\n" *3)
    print("欢迎下次光临")

    import os
    os._exit(0)
cmd_dict = {'a':add,'e':edit,'d':delete,'p':payment,'s':show_goods}
def show_command():
    cmd = input("请输入操作指令：\n" +
                "添加（a） 修改（e） 删除（d） 结算（p） 超市商品（s）\n")
    if cmd not in cmd_dict:
        print("命令错误")
    else:
        cmd_dict[cmd]()
init_repository()
show_goods()
while True:
    show_list()
    show_command()















































