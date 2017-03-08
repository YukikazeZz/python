#!/usr/local/bin/python
#_*_ coding:utf-8 _*_*
import random
def is_even_num(num):
    if num % 2==0:
        return True
    else:
        return False

def is_even_list(num):
    even_list=[]
    for i in range(num):
        if num % 2==0:
            even_list.append(i) 
    return even_list


if __name__ == '__main__':
    print("begin calculate even and print detail number:")
    a=int(raw_input("please input a number:"))
    num=random.randint(0,a)
    evenlist=is_even_list(num)
    print("print detail even number with list:",evenlist)
