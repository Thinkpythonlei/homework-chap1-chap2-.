# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:17:23 2022

@author: Surface
"""

#1.如果打印语句中少加了括号则会报出错误，错误的语句为：SyntaxError: EOL while scanning string literal
#2.如果打印语句中稍加了引号则会报出错误语句：SyntaxError: invalid syntax
#3.随便表示一个负数，正数前边加一个加号还会打印输出原来的那个数,2++2的结果为4
n1=-123
print(n1)
n2=+123
print(n2)
n3=2
n4=2
print(n3++n4)
#4.在数学中前导0没有问题，而如果在计算机中如果一个数据有前导0,那么这个数据是不被允许使用的。
#会报错，错误语句为：leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
#5.如果两个值之间没有运算符的结果会输出空
#n5=1
#n6=2
#print(n5n6)
#1.2
#(1)42分42秒等于多少秒
n8=42
n9=42*60
n10=n8+n9
print("42分42秒等于",n10)
#(2)10km换算成多少英里
n1=10
n2=n1/1.61
print('10km等于',n2,"英里")
#(3)42分42秒跑了10km则配速是多少（英里/时）
n1=2562
n2=3600
n3=10
n4=n3/1.61
n5=n4/(n1/n2)
print("配速为",n5,"英里/时")