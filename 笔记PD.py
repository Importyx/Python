import pandas as pd
import numpy as np

obj = pd.Series([1, 2, 3, 6, 5])
print('查看数组表现形式：', obj.values, ', 查看数组索引对象：', obj.index)

obj1 = pd.Series([1, 2, 3, 4, 5], index=['s', 'h', 'i', 'a', 'y'])
print('自己设定索引：\n', obj1)

obj2 = obj1[['a', 'h', 's', 'y']]
print('选择指定索引对象：\n', obj2)

obj3 = pd.Series(['blue', 'purple', ' yellow'])
obj3.reindex(range(6), method='ffill')
print(obj3)

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'b', 'c'], columns=['Ohio', 'Texas', 'California'])
print(frame)
frame = frame.reindex(['a', 'b', 'c', 'd'])
print(frame)
states = ['Texas', 'Utah', 'California']
states = frame.reindex(columns=states)
print(states)

x = states[states < 3]
print(x)

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

print(data)
data1 = data[['three', 'one']]
data2 = data[data['four'] > 6]
print('筛选four列大于6的数据集：\n', data2)

data3 = data < 7
print('判断data与7的关系，结果为布偶值，小于则为True，大于等于则为False：\n', data3)
data[data < 7] = 0
print('小于7的数据=0：\n', data)

print('选取Utah的two和four列：\n', data.loc['Utah', ['two', 'four']])
print('选取data的第三、二行的4、1、2列：\n', data.iloc[[3, 2], [3, 0, 1]])
print('截取列到Utah前，选取名为two的列：\n', data.loc[:'Utah', 'two'])
print('列都截取three列大于5的列，行截取到第三列：\n', data.iloc[:, :3][data.three > 5])

frame1 = pd.DataFrame(np.arange(12).reshape(4, 3,),
                      index=['Ohio', 'Colorado', 'Utah', 'New York'],
                      columns=list('bde'))
series3 = frame1['d']
print('frame1：\n', frame1, '\n', 'frame1的d列：\n', series3)
x1 = frame1.sub(series3, axis='index')
print('匹配行在列上广播：\n', x1)

x2 = np.abs(x1)
print('numpy的ufuncs也应用到pandas对象操作中：', x2)

!type 'examples/ex1.csv'
a,b,c,d,message
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo

df = pd.read_csv('example/ex1.csv')
print(df)