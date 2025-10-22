# ctrl+/添加注释或取消
# ctrl+d复制到下一行
#sep为分隔  如sep=，  就会用，分隔
#        ￥ print(123,345,323,sep='/')￥
#         输出为123/345/323
#float  小数
#int   整数
#bool   布尔型     固定写法 Ture和False  开头必须大写  前者相当于1 后者相当于0
#          ￥print(type(1.2)) 这种可以判断形式￥
#          输出为<class 'float'>


#%的用法
#%d代表输入出整数  %s代表输出字符串
 #           ￥    name='fucky'   ￥
 #                  age=20
 # print('id:%s,age:%d'%(name,age))
 #           输出为id:fucky,age:20

#         ￥  a='yuanshen'￥
#            b='3g'
#           print('game:%s,storage:%s'%(a,b))
#          输出为game:yuanshen,storage:3g
#          ######如上既有3这种整数又有g这种字符的表达都用%s（字符串）#########




 #格式化输出（最简单的代指法）
 #               ￥  a="cnm"￥
 #                   b=123
 #                 print(f"my name:{a},my code:{b}")





 #除出来求得的商形式为浮点数
 #“/”“//”“%”为除号
 #“//”除得的数一定为整数，直接舍去了小数点后的数
 #“%”除得的数是该除法计算式得出的余数
 #“**”代表幂，如3**2代表3的2次方
 #运算顺序：幂为最优先，其余是先乘除后加减，可用括号来改变优先级

 #赋值运算符——————不能全用已知的数字如print(5 += 4)
 #“+=”的运用
 #例：num1 += num2代表num1 + num2 = num1
 #“-=”同理




 #输入函数（input）
 #这样就可以在运行后的页面编写东西
#input("please print your name:")可单独写下这段，但没有反馈
#print("ok")此为附加，这样写就是反馈的内容







#转义字符
#\t制表符，两行都输会有对齐作用
#\n换行符，会换行
#\r回车，会将其后的内容改到开头，此时其前的内容会消失
#\\反斜杠，会取消后面斜杠能发挥的作用,最前面的斜杠不会消失
#在括号和引号之间添加r代表取消所有转义字符的作用
#             ￥  print(r"like you\ndo you know?")  ￥
#            输出为     like you\ndo you know?






#if判断
#a=input("please identify your answer,(A/B)")
#if a == 'A' :
#print("congratulations,you are correct")
#if a == 'B' :
 #print("you are error")

#a=input("请输入成绩：")                   #    !!!!!!    input中的内容默认为字符串，所以a==“100’必须有双引号，不管是否为数字，！！！！！！！
#if a=='100':
   # print("你真棒")
#if a=='60':
  #  print("还要继续加油哈")



#elif后接条件，可写多个elif生成多种情况
#if与else的循环运用及内部的if套娃

# fund="no"
# check='no'
# adjust='no'
# if fund == 'yes':
#  print("you are able to pay,so you cost it\n")
#  if check == "yes":
#   print("your computer is good\n")
#  else:
#   print("your computer is bad\n")
#  if adjust == 'yes':
#   print("smart\n")
#  else:
#   print("you are not able to pay\n")
# else:
#   print("slow\n")
#
#    将顶格写的内容看作文件夹，将空格写看作文件夹的子文件，两个顶格写就是两个不同且独立的文件夹。代码逻辑为：当fund=yes时会运行该文件夹同时会包括其子文件夹，当fund不等于yes时，就会运行其他文件夹
   # 也就是else   ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！







#!!!while循环语句！！！！累加   {for循环累加更简单}
#a=0
#i=1#在累加中初始值可以为0或1不影响计算结果
#while i <= 5:#代表i这个初始值如果小于5就要执行循环
 #a += i
 #i += 1#循环递增数要与print对齐，否则无法执行
 #print(a)
######for循环#######
########for的运用：拆分字符串########
#a="samkcmaklmckalm"#for能拆分字符串，无法拆分数字，故a只能等于字符串，若想拆分数字，必须给数字加上引号使其变为字符串
#for c in a:
#   print(c)
#######for与range#########列出range内部的存在的数   ！！所包含的数包含最小值，不包含最大值
# for a in range(0,10):
#    print(a)
# ########for的累加######
# c=0
# for a in range(0,101):!!!!!!!!!#print和c+=a处于同一缩进就会输出与其相同的性质，如此格式就会一个一个列出，若print顶格写就输出的只有答案
#     c += a
#     print("result:",c)
#######range语法#######
#range(5,10,2)中2代表递增为2，print输出将为5，7，9








#!!!!!!!模拟用户登录！！！！！！


#m=0
#while m<3:
 #a=input("用户名:")
 #b=input("密码：")
 #if a=="bj" and b=="bj520":                               #iiiijdilvnjsdnvjnvmd cnvm
    #print("账号登陆中.....")
    #m=8
 #else:
  #if m < 2:
    #print("密码错误，请重新输入！剩余",2-m,"次机会")                #fsbfdgsfgsdfadk,fmn,kasnfn
  #m+=1
  #if m == 3:
    #print("你的账号已被锁定！")

#模拟登录
#a=0
#while a<3:
    #w=input("id:")
    #e=input("code:")
    #if w=="bj" and e=="bj520":
      #print("logging in.....")
      #a=8
    #else:
     #if  a<2:
        #print("you are able to input",2-a,)
     #a+=1
#if a == 3:
    #print("beg to login!")




#a=0
#while a<3:
    #w=input("id:")
    #e=input("code:")
    #if w=="bj" and e== "bj520":
        #print("login in.......")
        #a=8
    #else:
      #if a<2:
         # print("code or id is error,you are only have",2-a,)
    #a += 1
    #if a == 3:
        #print("the id is beg to login!")


#a = 0
#while a < 3:
    #w = input("id")
    #e = input("code")
    #if w == "bj" and e == "bj520":
        #print("login.....")
        #a = 5
    #else:
        #if a < 2:
            #print("the code is error.you only to input", 2 - a, )
        #a += 1
    #if a == 3:
        #print("beg to input!!!")

#在print内的字符串后输入end=""就不会换行
#print()代表回车换行
######九九乘法表######
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{i}*{j}={i*j}\t",end="")
#         j+=1
#     i+=1
#     print()

#continue与break
# for w in range(1,4):
#     print(0)
#     for e in range(1,3):
#      print(1)
#      continue#---------->中断print（2）的输出，其他照常
#      print(2)
# print(3)

# for w in range(1,4):
#     print(0)
#     for e in range(1,3):
#      print(1)
#      break#---------->中断print(2)并使break所在的层中的for的循环作用失效(相当于删除第238行后的效果）
#      print(2)
# print(3)
