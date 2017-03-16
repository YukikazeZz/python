#!/usr/bin/python
from __future__ import print_function
import string

def valid_password(pwd):
    if len(pwd)< 2  or len(pwd)>10:
        return False
    if pwd[0] not in string.ascii_letters:
        return False
    for char in pwd:
        if  char not in string.digits + string.ascii_letters + '_':
            return False
    if pwd[-1] in '_':
        return False
    return True
        

if __name__== "__main__":
    pwd=raw_input("put your passwd:")
    print(valid_password(pwd))
