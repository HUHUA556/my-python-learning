#####if  else #######
# print("欢饮来到黑马游乐场，成人收费，儿童免费")
# a=input("请输入你的年龄：")
# if a>="18":
#     print("您已成年，游玩需补票10元。\n祝你游玩愉快！")
# else:
#     print("你未成年，可免费游玩")




####九九乘法表#####
# i = 1
# while i <= 9:
#     j = 1                                              #内循环无论j变为了多少都会从初始值开始
#     while j <= i:
#         print(f"{j}*{i}={j*i}\t",end="")
#         j += 1
#     i+=1
#     print()




######数a+遍历#######
# w="itheima is brand of itcast"
# i=0
# for e in w:
#     if e == "a":
#         i+=1
#     print(e)
# print(f"w中含有{i}个a")





#######数偶数########
# s=0
# for e in range(1,101):
#     if e%2==0:
#      s+=1
#      print(e)
# print(s)







######for循环嵌套#######
# e=0
# for e in range(1,101):
#     print(f"day:{e}")
#     for i in range(1,11):
#         print(f"render:{i}")
#     print("give you")
# print("make it")








########for循环的九九乘法表########
# for e in range(1,10):
#     for n in range(1,e+1):
#         print(f"{n}*{e}={n*e}\t",end="")
#     print()

   # !!!!!!!试错方式理解！！！！！
   #如上刚开始会在内循环的range中写（1，10）经过推算发现这样会变成1*1 2*2 3*3。。。。。。等
   #我们需要的是：
   #当e等于2时内循环中只出现1，2（即循环范围的数为两个数就终止）
   #当e等于3时内循环中只出现1，2，3（即循环范围的数为三个数就终止）
   #显然写（1，10）时当e等于任何数时都会是范围为10的循环数（即1，2，3，4，5，6，7，8，9，）即输出为第一行所示内容
   #故range中的范围是必须要时刻变化的并且随e的变化而变化，所以在range中引入e这个非总是循环的变量
   ###“引入变量”思想###


########模拟登录########

# c=1
# while c<=3:
#     a=input("please input id:")
#     b=input("please input your code:")
#     if a=="bj" and b=="bj520":
#         print("login.....")
#         c=4
#     else:
#         if c<3:
#          print("the code or id is error,you only to input",3-c,)
#         c+=1
# if c==4:
#     print("the account is locked!!!!")


#修改实验
