def loginGUI():
    print("     欢迎试用丰翼超市管理系统      ")
    print("***********************************")
    print("      1.登录系统")
    print("      2.退出系统")
    print("***********************************")
    op = input("请输入您的选择:")
    if op == "1":
        login_check()

    elif op == "2":
        exit()
    else:
        print("请输入正确选择！！")
        loginGUI()


def add_goods(good):
    name = input("请输入商品名称：")
    count = input("请输入商品数量：")
    price = input("请输入商品单价：")
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    print("         商品名称：" + name)
    print("         商品数量：" + count)
    print("         商品单价：" + price)
    print("***********************************")
    good.append({"商品名称": name, "商品数量": count, "商品单价": price})
    op = input("添加成功！切q键返回:")
    if op == "q":
        goods_manage(good)


def delete_goods(good):
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    name = input("请输入商品名称：")
    flag = 0
    for i in range(0, len(good)):
        if name == good[i]["商品名称"]:
            flag = 1
            op = input("输入y键删除：")
            if op == "y":
                good.pop(i)
                print("删除成功")
                goods_manage(good)
    if flag == 0:
        op = input("没有找到对应商品，请重新输入（按q键返回）：")
        if op == "q":
            delete_goods(good)
    print("***********************************")


def show_goods(good):
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    for i in range(1, len(good) + 1):
        print(str(i) + "." + good[i - 1]["商品名称"] + "   库存" + good[i - 1]["商品数量"] + "个，单价" + good[i - 1][
            "商品单价"] + ",合计：" + str(int(good[i - 1]["商品数量"]) * int(good[i - 1]["商品单价"])))
    print("***********************************")
    op = input("按q键返回：")
    if op == "q":
        goods_manage(good)
    else:
        print("请按要求输入！")
        show_goods(good)


def goods_manage(good):
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    print("         1.添加商品")
    print("         2.删除商品")
    print("         3.显示所有商品")
    print("         4.返回上一级")
    print("***********************************")
    op = input("请输入您的选择：")
    if op == "1":
        add_goods(good)
    elif op == "2":
        delete_goods(good)
    elif op == "3":
        show_goods(good)
    elif op == "4":
        login_success()
    else:
        print("请输入正确选择！！")
        goods_manage(good)


def add_membership(member):
    name = input("请输入会员姓名：")
    integral = input("请输入会员积分：")
    tel = input("请输入会员电话：")
    number = input("请输入会员编号(年+月+日+小时+分钟+00001)：")
    member.append({"会员编号": number, "会员姓名": name, "会员积分": integral, "会员电话": tel})
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    print("         会员编号:" + number)
    print("         会员姓名:" + name)
    print("         会员积分:" + integral)
    print("         会员电话:" + tel)
    print("***********************************")
    op = input("添加成功，按q键返回上一级：")
    if op == "q":
        Membership_manage()
    else:
        print("请按要求输入！")
        add_membership(member)


def delete_membership(member):
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    flag = 0
    number = input("请输入会员编号：")
    print("***********************************")
    for i in range(0, len(member)):
        if number == member[i]["会员编号"]:
            flag = 1
            break
    if flag == 1:
        op = input("确定要删除吗？按y删除，q返回上一级：")
        if op == "y":
            for i in range(0, len(member)):
                if number == member[i]["会员编号"]:
                    member.pop(i)
                    break
        elif op == "q":
            Membership_manage()
        else:
            print("请按要求输入！")
            delete_membership(member)
    else:
        op = input("该会员编号不存在，重新输入请按y，返回上一级请按q：")
        if op == "y":
            delete_membership(member)
        elif op == "q":
            Membership_manage()
        else:
            print("请按要求输入！")
            delete_membership(member)


def show_membership(member):
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    print("编号 姓名 积分 电话")
    for i in range(0, len(member)):
        print(member[i]["会员编号"] + "  " + member[i]["会员姓名"] + "  " + member[i]["会员积分"] + "  " + member[i]["会员电话"])
    print("***********************************")
    op = input("按q返回上一级：")
    if op == "q":
        Membership_manage()
    else:
        print("请按要求输入！")
        show_membership(member)


def checkout(good):
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    total = 0
    flag = 0
    kind = input("请输入商品种类数：")
    if int(kind) <= len(good):
        for j in range(0, int(kind)):
            name = input("商品名称：")

            for i in range(0, len(good)):
                if name == good[i]["商品名称"]:
                    number = input("商品数量：")
                    if int(number) <= int(good[i]["商品数量"]):
                        flag = 1
                        total = total + int(good[i]["商品单价"]) * int(number)
                        print("商品名称   数量  单价   应收   ")
                        print(name + "  " + number + "  " + good[i]["商品单价"] + "  " + str(
                            int(good[i]["商品单价"]) * int(number)))
                    else:
                        print("超出库存！请重新输入！")
                        checkout(good)
            if flag == 0:
                print("该商品不存在请重新输入！")
                checkout(good)
    else:
        print("超出库存！请重新输入！")
        checkout(good)
    print("==============================")
    print("合计：     " + str(total))
    print("***********************************")
    op = input("按q返回上一级：")
    if op == "q":
        login_success()
    else:
        print("请按要求输入！")
        checkout(member)


def Membership_manage():
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    print("         1.添加会员")
    print("         2.删除会员")
    print("         3.显示所有会员")
    print("         4.返回上一级")
    print("***********************************")
    op = input("请输入您的选择：")
    if op == "1":
        add_membership(member)
    elif op == "2":
        delete_membership(member)
    elif op == "3":
        show_membership(member)
    elif op == "4":
        login_success()
    else:
        print("请输入正确的选择！")
        Membership_manage()


def login_success():
    print("     欢迎试用丰翼超市管理系统     你好！ admin ")
    print("***********************************")
    print("         1.商品管理")
    print("         2.会员管理")
    print("         3.结账")
    print("         4.退出系统")
    print("***********************************")
    op = input("请输入您的选择：")
    if op == "1":
        goods_manage(good)
    elif op == "2":
        Membership_manage()
    elif op == "3":
        checkout(good)
    elif op == "4":
        exit()
    else:
        print("请输入正确选择！！")
        login_success()


def login_check():
    username = input("请输入用户名：")
    userpwd = input("请输入密码：")
    if username == "admin" and userpwd == "123456":
        login_success()
    else:
        print("请输入正确的用户名和密码：")
        login_check()


member = []
good = []
loginGUI()
