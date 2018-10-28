# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:10:21 2017

@author: Administrator
"""
#%% spyder常用快捷键
'''
　　Ctrl + 1: 注释/反注释

　　Ctrl + 4/5: 块注释/块反注释

　　Ctrl + L: 跳转到行号

　　Tab/Shift + Tab: 代码缩进/反缩进

　　Ctrl ＋I：显示帮助
'''
#%% 分节
# In[]分节
#%% 有用的命令
#删除变量，导入的东西
%reset
#%% spyder调试与变量浏览器
'''
只会显示当前文件\模块中的变量，另外tensorflow中的变量无法显示
'''
#%%自动重载：
## Some more magic so that the notebook will reload external python modules;
## see http://stackoverflow.com/questions/1907993/autoreload-of-modules-in-ipython
get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')

#%% numpy使用注意
'''
基础知识
https://docs.scipy.org/doc/numpy/user/quickstart.html#the-basics
'''
#%%广播
#http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc
#%%矩阵阶数对索引和广播broadcast的影响
#行或列向量阶数为1：（n，）与矩阵阶数为2：（n,1）
import numpy as np
a=np.array([1,2,3])
b=a.reshape((-1,1))
print(a[0])
print(a[1])
tmp1=a[1]
#print(a[0,0])  #IndexError: too many indices for array
print(b[1])  #阶数为2的数组用一个用一维索引，默认第二维是所有元素
tmp2=b[1:3]
tmp3=b[1]
print(b[0,0])

#对广播broadcast的影响
m=np.tile(a,(4,1)) #shape(4,3)
c=b.T
m1=m+a   #广播对阶数为1的向量要求(4,3) (3,) 广播时把向量变为(1,3)
a=np.array([1,2,3,4])#operands could not be broadcast together with shapes (4,3) (4,) 
#m2=m+b  #ValueError: operands could not be broadcast together with '
         #shapes (4,3) (3,1) 
m3=m+c   # 广播对阶数为2的数组要求不为1的轴尺寸相同
         #shapes (4,3) (1,3)
#%%矩阵运算
'''
小结：
严格按照矩阵运算法则
(n,)一维数组
(n,1)二维数组
有一个运算对象为一维数组:You can treat one-dimensional arrays as 
either row or column vectors. dot(A,v) treats v as a column vector, 
while dot(v,A) treats v as a row vector. 
'''
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.array([[1,2],[3,4],[5,6]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))#(2,)*(2,)
print(np.dot(v, w))

vv=v.reshape((-1,1))
print(vv)

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))#(2,2)*(2,)=(2,)
print(np.dot(x, v))
print(x.dot(vv))#(2,2)*(2,1)=(2,1)
print(x.dot(vv.T))#(2,2)*(1,2) ValueError: shapes (2,2) and (1,2) not aligned: 2 (dim 1) != 1 (dim 0)
print(z.dot(v))#(3,2)*(2,)=(3,) 
print(v.dot(z))#(2,)*(3,2)ValueError: shapes (2,) and (3,2) not aligned: 2 (dim 0) != 3 (dim 0)
print(v.dot(z.T))#(2,)*(2,3)=(3,)
 
# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
#%%  函数使用时的轴:axis=0是
import numpy as np
x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"
#%%求集合中的众数
import numpy as np
a=np.array([1,2,3,2])

from collections import Counter
c = Counter(a)
mode_a = c.most_common(1)[0][0]