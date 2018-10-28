# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:42:27 2017

@author: Administrator
"""

# file two.py
import one        # start executing one.py

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")