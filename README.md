task1.class数据集的训练

1.SEX 男女各几人 

2.分sex下weight height 分布

3.分sex, age下 weight, height 分布

4.建图x age, age, height
      y height, weight, weight
      
5.建立一个回归方程weight age height 



task2.class数据集的训练

1.分sex-weight.mean-sex---表A
             height.mean-sex---表B

2.class 将class、表A、表B以Sex进行合并，Join或者Merge

3.新建两列空数据，ID分别为overweight、overheight
用IF进行的判定，

IF weight>weight.mean-sex 则 overweight=1
else overweight=0；
height>height.mean-sex 则 overheight=1
else overheight=0；

4.overweight为y，overheight、age、sex为x
进行logistic regression回归

5.对19列样本数据进行overweight的预测，计算其准确性
