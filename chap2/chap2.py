# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:08:10 2022

@author: Surface
"""

#n=42是合法的，42=n不合法。因为数字不可以在计算机语句的第一位，1n不合法，而n1就是合法的。
#x=y=1是合法的
x=y=1
print(x)
print(y)
#下面语句是按照冒号结尾的python合法语句，若以分号结束则会报错，错误语句是SyntaxError: invalid character '；' (U+FF1B)
import turtle
circle=turtle.Turtle()

def polygon(t,n,length):
    angel=360/n
    for i in range(n):
        t.fd(length)
        t.lt(angel)
polygon(circle,100,5)

#import turtle
#circle=turtle.Turtle()

#def polygon(t,n,length)；
    #angel=360/n
    #for i in range(n)；
        #t.fd(length)
        #t.lt(angel)
#polygon(circle,100,5)
#语句的结尾以分号结束，以最简单的例子来操作,结果不会受到影响。
x=1
print(x);
#在python中如果不加运算符号直接相乘则会报错NameError: name 'xy' is not defined




#2.2计算半径为5的球体的体积：
import math
r=5
v=math.pi*(4/3)*r**3
print("半径为5的球体的体积为",v)
#购书问题：
n1=24.95*0.6*60
n2=3+0.75*59
n3=n1+n2
print("购买60本书的总价是",n3,"$")
#跑步回家什么时候吃饭问题：
n1=15*2+12*3#(总共耗费的秒数)
n2=8*2+7*3#(总共耗费的分钟数)
if n1>60:
    n3=n1/60
    n4=n1%60
    n3=int(n3)
else: n1=0
n5=n3+n2+52
n6=n5-60
n7=n5/60+6
n7=int(n7)
print("回到家吃早餐的时间为",n7,"时",n6,"分",n4,"秒")































