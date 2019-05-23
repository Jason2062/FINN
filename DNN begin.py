# -*- coding: utf-8 -*-
"""
y = w * x + b
通过随机x训练，求w，b
"""

import numpy as np  #导入模块numpy，并以np作为别名
rw = 0.7 # true w = 0.7
rb = 0.5 # true b = 0.5

w = 123 # random value
b = 456 # random value
lr = 0.4 # learning rate, change w and b to make it
for step in range(1000): # 0 1 2 ... 599
       x = np.random.random(1) # random number
       y_data = x * 0.7 + 0.3  # real value
       y = w * x + b           # value to be trained
       loss = y - y_data       # loss function
       w -= lr * x * loss      # w = w - Lr * x * loss
       b -= lr * loss          # b = b - lr * loss
       if step % 20 == 0:
           print(step, loss, w, b) # print medium valuw

print (step, loss, w, b) #final trained value


