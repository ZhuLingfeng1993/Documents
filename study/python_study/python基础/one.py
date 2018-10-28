# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:40:01 2017

@author: Administrator
"""

# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")