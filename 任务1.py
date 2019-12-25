import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
# 导入所需数据库

# 第一问：按性别分类并计数
df = pd.read_csv('CLASS1.csv')
print('数据种类:\n', df.dtypes)
# 导入数据、检查数据种类

print('男女样本个数:\n', df["Sex"].value_counts())
# 选择性别并计数

# 第二问：不同性别下的身高体重分布
df_sex = df[['Sex', 'Height', 'Weight']]
df_male = df_sex[df_sex["Sex"] == "男"]
df_female = df_sex[df_sex["Sex"] == "女"]
# 男、女的身高体重数据

print('男性身高体重分布：\n', df_male.describe())
print('女性身高体重分布：\n', df_female.describe())
# 男女的身高体重分布


for i in df[['Sex', 'Age', 'Height', 'Weight']].groupby(['Sex', 'Age']):
    print(i)
# 不同性别、年龄下身高体重的数据

# 第三问：不同性别、年龄下身高体重的分布
df_sex_age = df[['Sex', 'Age', 'Height', 'Weight']].groupby([df['Sex'], df['Age']]).describe()
print('不同性别、年龄下身高体重的分布:\n', df_sex_age)
# 不同性别、年龄下身高体重的分布

df_male = df[df["Sex"] == "男"]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for c, m in [('r', 'o')]:
    xs = df_male[['Age']]
    ys = df_male[['Height']]
    zs = df_male[['Weight']]
    ax.scatter(xs, ys, zs, c=c, marker=m)
# 男性的年龄身高体重的分布图

df_female = df[df['Sex'] == "女"]
for c, m in [('b', '*')]:
    xs = df_female[['Age']]
    ys = df_female[['Height']]
    zs = df_female[['Weight']]
    ax.scatter(xs, ys, zs, c=c, marker=m)
# 男性的年龄身高体重的分布图

ax.set_xlabel('Age')
ax.set_ylabel('Height')
ax.set_zlabel('Weight')
# 添加坐标

plt.title('Age, Height, Weight')
plt.savefig('D:\Figure\Task1\AHG.jpg', dpi=400)
plt.show()
# 不同性别的年龄身高体重的分布图

# 第四问：建图，x分别为age，age，height y分别为height weight, weight
fig = plt.figure()
ax_age_height = fig.add_subplot(2, 2, 1)
ax_age_weight = fig.add_subplot(2, 2, 2)
ax_height_weight = fig.add_subplot(2, 2, 3)

ax_age_height.scatter(df['Age'], df['Height'], marker='v', c='g')
ax_age_height.set_title('Age And Height')
ax_age_height.set_xlabel('Age')
ax_age_height.set_ylabel('Height')
plt.xlim(10.15)
plt.ylim(70.150)
# Age,Height散点图

ax_age_weight.scatter(df['Age'], df['Weight'], marker='o', c='r')
ax_age_weight.set_title('Age And Weight')
ax_age_weight.set_xlabel('Age')
ax_age_weight.set_ylabel('Weight')
# Age,Weight散点图

ax_height_weight.scatter(df['Height'], df['Weight'], marker='*', c='y')
ax_height_weight.set_title('Height And Weight')
ax_height_weight.set_xlabel('Height')
ax_height_weight.set_ylabel('Weight')
# Height,Weight散点图

plt.savefig('D:\Figure\Task1\Scatters.jpg', transparent=True, dpi=400, pad_inches=0)
plt.show()
# 第四问：做图

# 第五问：建立关于weight的回归方程
data = df[['Age', 'Height', 'Weight']]
print('回归数据\n', data)
# 导入回归数据

print('回归数据分布\n', data.describe())
# 数据描述性统计
print(data[data.isnull() == True].count())
# 空缺值
data.boxplot()
plt.savefig('D:\Figure\Task1\Boxplot.jpg')
plt.show()
# 箱型图
print('回归数据相关系数\n', data.corr())
# 数据相关系数

sns.pairplot(data, x_vars=['Age', 'Height'], y_vars='Weight', size=19, aspect=0.8, kind='reg')
plt.savefig('D:\Figure\Task1\Pairplot.jpg')
plt.show()
# 使用Seaborn的Pairplot来查看年龄身高对体重的影响，通过加参数kind='reg'，可以添加一条最佳拟合直线和95%的置信带

X = data[['Age', 'Height']]
Y = data[['Weight']]
# 设定变量与自变量

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
# 选取所需数据，划分测试集、训练集

model = linear_model.LinearRegression()
# 定义模型

model.fit(X_train, Y_train)
print('最佳拟合线：截距', model.intercept_, '，回归系数', model.coef_)
# 得出训练集模型的参数

acc = model.score(X_test, Y_test)
print('模型准确率:', acc)
# 查看在测试集的准确率

Y_pred = model.predict(X_test)

print('Y的预测值\n', Y_pred)
plt.plot(range(len(Y_pred)), Y_pred, marker='s', linestyle='--', c='g', label='predict')
# 显示图像
plt.title('Prediction line')
plt.savefig('D:\Figure\Task1\Predict.jpg')
plt.show()


plt.figure()
plt.plot(range(len(Y_pred)), Y_pred, marker='8', linestyle='-', c='k', label="predict")
plt.plot(range(len(Y_pred)), Y_test, marker='^', linestyle='-', c='m', label="test")
plt.legend(loc='upper right')
# 显示图中的标签
plt.xlabel('Number of weights')
plt.ylabel('Value of weights')
plt.title('ROC')
plt.savefig('D:\Figure\Task1\ROC.jpg')
plt.show()
# 绘制ROC曲线
