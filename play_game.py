#!/usr/local/bin/python
#_*_ coding:utf-8 _*_*
import random
def play_game(num):
    while True:
        a=raw_input("please input a number:")
        if a.isdigit():
            if int(a)>num:
                print("you are bigger")
            
            elif int(a)<num:
                print("you are smaller")

            else:
                print("you are right,play game number is",int(a))
                a=raw_input("do you continue to play again,please input [yes/no]:")
                if a.upper()=='YES':
                    continue
                elif a.upper()=='NO':
                    print("do you realy to play game now")
                    a=raw_input("do you want to exit play,please input [yes/no]")
                    if a.upper()=='YES':
                        print("you exit to play game now")
                        break
                    else:
                        print("your input is not exit,game will continue")
                        continue 
                else:
                    print("your input nit in [yes/no],i will return play game") 
                    continue  
        else:
            print("your input is not number,please put a number:")
            continue 

def main():
    print("--------begin game---------")
    num=random.randint(0,99)
    play_game(num)


if __name__ == '__main__':
    main()
