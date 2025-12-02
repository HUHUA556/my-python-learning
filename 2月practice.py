# 定义一个全局变量：money，用来记录银行卡剩余金额
# 定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
# 定义如下函数：
#     》查询余额函数
#     》取款函数
#     》存款函数
#     》主菜单函数
# 要求：
#     程序启动后要求输入用户姓名
#     查询余额，存款，取款后，都会返回从主菜单
#     存款取款后都会显示当前余额
#     除非客户选择退出，否则程序会一直运行

#实操

#输出初始欢迎语
"""""""""""
money=5000
name=None
name=input("please input your name:")
print(f"hello,{name}")
"""""""""""
#定义一个查询函数
"""""""""""
def inquiry():
    print("             [inquiry fund]              ")
    global money
    print(f"your account's fund:{money} ")
"""""""""""
#定义一个取款函数
"""""""""""
def take_out_fund():
    print("             [take out fund]              ")
    global money
    a=int(input("please input taking out fund:"))
    if a<=5000:
     money-=a
     print(f"take out that success,the account's fund:{money}")
    else:
        print("your account's fund is insufficient")
"""""""""""

#定义一个存储函数
"""""""""""
def save():
    print("               [save fund]              ")
    global money
    c=int(input("please input saving fund:"))
    money+=c
    print(f"save that success,the account's fund:{money}")
"""""""""""

#定义一个菜单函数
"""""""""""
def main_menu():
     print("---------------main menu----------------")
     print("inquiry fund that press '1'")
     print("take out fund that press '2'")
     print("save fund that press '3'")
     print("Exit that press '4'")
     return input("please select your serve")
"""""""""""
#设置无限循环，使每次进行完一个服务后都会返回主菜单
"""""""""""
while True:
    l=main_menu()            #此处将main_menu=l，是将你输入的结果保存起来，保存到l函数中，如果直接输入main menu（）
#                                                                                        if main menu（）='1'
#                                                                                            inquiry（）
    if l =="1":
        inquiry()                                                                   #    那么输出就会一直为主菜单而不是调用函数
                                                                                    #    因为1没有被保存，if接收后立马将1丢失
                                                                                    #    if发现你输入的为空白就不会调用函数，然后
    elif l=="2":                                                                    #    开启下一轮循环也就是从main menu开始
        take_out_fund()

    elif l=="3":
        save()

    elif l== "4":
        print("Exit....\nfinish!")
        break
    else:
        print("Invalid choice,please try again")
"""""""""""""""


















