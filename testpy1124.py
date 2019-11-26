# -*- coding: utf-8 -*-
print(123)
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
x = np.arange(1,11)
y =  2  * x +  5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x,y)
# plt.show()


a = np.arange(6)
print ('我们的数组是：')
print (a)
print ('调用 id() 函数：')
print (id(a))
print ('a 赋值给 b：')
b = a
print (b)
print ('b 拥有相同 id()：')
print (id(b))
print ('修改 b 的形状：')
b.shape =  3,2
print (b)
print ('a 的形状也修改了：')
print (a)

import numpy.matlib
import numpy as np
print '234'
print (np.matlib.empty((2,2)))
