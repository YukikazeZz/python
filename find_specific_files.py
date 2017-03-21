#!/usr/bin/python
import os


def find_specific_files(root):
    result=[]
    for root,dirnames,filenames in os.walk(root):
        for filename in filenames:
            result.append(os.path.join(root,filename))

    return result

print(find_specific_files('.'))
