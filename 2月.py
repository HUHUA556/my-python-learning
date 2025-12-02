#函数的应用
#函数的定义
#def 函数名（参数）
    # 函数体

#如果定义了一个函数，此时没有写调用，那么该定义了的函数的函数体将不会执行
#return 后面所接的代码例如return input（“word”）代表将input加入return所在的函数中，在调用该函数时会执行input该有的键盘录入


#不使用len（）来统计字符串有几个字母
#实例一：
"""""""""
a="abcdefj"
b="hijklmn"
c="opqrstu"
i=0
for r in a:
    i+=1
print(f"{i}")
i=0
for t in b:
    i+=1
print(f"{i}")
i=0
for j in c:
    i+=1
    print(f"{i}")
"""""""""
#实例二：（去除上方的重复性输入方法）
"""""""""
b="dasdkma"
f="skmldas"
p="kasdsmfkl"
def a(data):
   e=0
   for i in data:
     e+=1
   print(f"{e}")

a(b)
a(f)
a(p)
"""""""""""""


#函数参数应用
""""""
def a(x,y):
    print(f"{x}*{y}={x*y}")
a(1,2)

def a(t):
    print("engage in check...")
    if 36.1<=t<=37.5:
      print(t)
      print("the temperature is normal")
    else:
      print(t)
      print("the temperature is abnormal")
a(37)
"""""""""""
# 函数返回值应用
"""""""""""
# def a(c,f):
#     o=c*f
#     return o
#     print("ok")-------->与return同列代码不会执行
# l=a(2,3)
# print(l)
"""""
# 函数调用
"""""""""""
# def a():
#     print("ccss")     #输出顺序：jjkk
# def b():              #        ccss
#     print("jjkk")     #        hhss
#     a()
#     print("hhss")
# b()
#
# （先调用哪个函数就会先输出哪个函数）内部先不用看，上述先调用的是b（）故从def b（）开始

"""""""""




#数据容器
#列表：list
"""
name=["cd",222,False]
print(name)
print(type(name))
#输出为：
['cd', 222, False]
<class 'list'>
"""
#列表可存储多个数据，且可以为不同的数据类型，如上有布尔，整型与字符串，也支持嵌套：
"""
name=[[123,"bu",True],[223,"a"]]
print(name)
输出为
[[123,"bu",True],[223,"a"]]
"""

#列表及其下标索引
#如何从列表中取出特定位置的数据：
#例子：
"""
a=[123,"bu",True]
print(a[0])
print(a[1])
print(a[2])

输出为：
123
bu
True
"""
#嵌套列表的数据取法：
#实例：
"""""""""
a=[[123,[444,555]],["bu","cc"],[True,False]]
print(a[0][1][1])
print(a[2][0])

#输出为：
#555
#True
"""
#以此类推


#运用index来查询元素在列表的下表索引（对嵌套列表无用）
"""
a=[123,444,555,"bu","cc",True,False]
index=a.index("bu")
print(index)
输出为：
3
"""

#修改列表内的元素
"""
a=[123,444,555,"bu","cc",True,False]
a[3]="ccccc"
print(a)
输出为：
[123, 444, 555, 'ccccc', 'cc', True, False]
"""

#运用insert在列表中插入元素
#如下括号内如果是1，那么就会出现在索引为0的元素的后面
"""
a=[123,444,555,"bu","cc",True,False]
a.insert(1,"mmmm")
print(a)
#输出为：
[123,"mmmm"，444,555,"bu","cc",True,False]
"""

#运用append在列表结尾追加一个元素
"""
a=[123,444,555,"bu","cc",True,False]
a.append("gggg")
print(a)
#输出为：
[123, 444, 555, 'bu', 'cc', True, False, 'gggg']
"""