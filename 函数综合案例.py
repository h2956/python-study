
money = 5000000
name = input("请输入姓名")
inp = 0

def c():
    """
    c函数可以打开菜单，对银行系统操作进行选择，查询余额，存款，取款，退出
    :return: 无
    """
    print("----------菜单----------")
    print(f"{name}，您好，欢迎来到银行ATM，请选择操作：")
    print("查询余额[输入1]\n存款[输入2]\n取款[输入3]\n退出[输入4]\n")
    global inp
    inp = input("请输入您的选择：")
    while 1:
        if inp == "1":
            d()
        elif inp == "2":
            e()
        elif inp == "3":
            f()
        elif inp == "4":
            print("退出成功")
            break
        else:
            print("输入错误，请重新输入")
            inp = input("请输入您的选择：")


def d():
    """
    d函数用来进行查询余额
    :return: 无
    """
    print("-----查询余额-----")
    print(f"{name},您好，当前的余额是{money}")
    c()

def e():
    """
    e函数用来进行存款
    :return: 无
    """
    print("-----存款-----")
    money_1 = 0
    money_1 = input()
    print(f"{name}，您好，您存款{money_1}元成功")
    global money
    print(f"{name}，您好，您的余额剩余：{money + int(money_1)}元")
    money = money + int(money_1)
    c()

def f():
    """
    f函数用来进行存款
    :return: 无
    """
    print("-----取款-----")
    money_2 = 0
    money_2 = input()
    print(f"{name},您好，您取款{money_2}元成功")
    global money
    print(f"{name}，您好，您的余额剩余：{money - int(money_2)}元")
    money = money - int(money_2)
    c()


if inp != 4:
    c()
