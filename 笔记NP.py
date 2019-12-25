import numpy as np

# Generate some random data
data = np.random.randn(2, 3)
print(data)

data = data * 10
print(data)

data = data + data
print(data)

print('数列结构:', data.shape)
print('数据类型：', data.dtype)
print('数列属性：', type(data))
# 查看结构，数据类型，属性

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print('转化数据形式：', arr1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print('转化数据形式：', arr2)
# ndarray化数组

print(arr2.ndim)
print(arr2.shape)
# 查看维度

print(np.zeros(10))
print(np.zeros((2, 3, 4)))
# 创建0数列，维度从高到低

print('arrange生成数组形式:', np.arange(15))

arr1 = np.array([1, 2, 3], dtype=np.float)
arr2 = np.array([4, 5, 6], dtype=np.int32)
print('转化为ndarray数据时，设置数据类型：', arr1.dtype, ',', arr2.dtype)

arr3 = np.array([11, 12, 13, 14, 15])
float_arr = arr3.astype(np.float64)
print('将arr3的int数据类型转化为float_arr的float64，字符串类型的数字也可以转化为float或int类的数字:\n', arr3.dtype, ',', float_arr.dtype)

arr4 = np.array([1.1, 2.2, 3.3, 4.4])
int_arr = arr4.astype(np.int)
print('将arr4的float数据类型转化为int_arr的int时小数部分会被删除', int_arr)

import matplotlib.pyplot as plt
import random
postion = 0
walk = [postion]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    postion += step
    walk.append(postion)

plt.plot(walk[:100])
plt.show()
