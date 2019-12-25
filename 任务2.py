import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# 导入模块

file = "CLASS1.csv"
df = pd.read_csv(file)
data = df[["Sex", "Age", "Height", "Weight"]]
# 导入数据

male = df[df['Sex'] == '男']
female = df[df['Sex'] == '女']
# 男女数据分类

male_mean_height = male['Height'].mean()
male_mean_weight = male['Weight'].mean()
female_mean_height = female['Height'].mean()
female_mean_weight = female['Weight'].mean()
# 男女平均身高体重数据

a = {'Sex': '男', 'Height_mean': male_mean_height, 'Weight_mean': male_mean_weight}
a1 = pd.DataFrame([a])
b = {'Sex': '女', 'Height_mean': female_mean_height, 'Weight_mean': female_mean_weight}
b1 = pd.DataFrame([b])
Sex_mean = pd.concat([a1, b1], axis=0, ignore_index=True)
print('男女的平均身高、体重：\n', Sex_mean)
# 第一题男女的平均身高、体重表

data_sex_mean = pd.merge(data, Sex_mean)
print('男女的身高体重数据：\n', data_sex_mean)
# 第二题男女的身高体重以及平均数据

overheight_list = []
for line in data_sex_mean.values:
    overheight_list.append(1) if float(line[2]) > float(line[4]) else overheight_list.append(0)
data_sex_mean['Overheight'] = overheight_list

overweight_list = []
for line in data_sex_mean.values:
    overweight_list.append(1) if float(line[3]) > float(line[5]) else overweight_list.append(0)
data_sex_mean['Overweight'] = overweight_list
print('身高体重超过平均数的判断：\n', data_sex_mean)
# 第三题男女身高体重超过平均值的判断

sex_list = []
for line in data_sex_mean.values:
    sex_list.append(True) if str(line[0]) == "男" else sex_list.append(False)
data_sex_mean['Sex_bool'] = sex_list
# 把性别转换为bool

data_reg = data_sex_mean[['Sex_bool', 'Age', 'Overheight', 'Overweight']]
print('相关系数矩阵：\n', data_reg.corr())

X = data_reg[['Sex_bool', 'Age', 'Overheight']]
Y = data_reg[['Overweight']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=0)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, Y_train)
print('最佳拟合线系数：', model.coef_, '截距：', model.intercept_)
# 第四问模型的测试结果、系数、截距

acc = model.score(X, Y)
print('模型准确率：', acc)
# 第五问模型对19个样本数据的预测的准确率

Y_pre = model.predict(X_test)
print('Y的预测值：\n', Y_pre)

plt.figure()
plt.plot(range(len(Y_pre)), Y_pre, marker='8', linestyle='-', c='k', label="predict")
plt.plot(range(len(Y_pre)), Y_test, marker='^', linestyle='-', c='m', label="test")
plt.legend(loc='upper right')
# 显示图中的标签
plt.xlabel('Number of overweights')
plt.ylabel('Value of overweights')
plt.title('ROC')
plt.savefig('D:\Figure\Task2\ROC.jpg')
plt.show()
# 绘制ROC曲线