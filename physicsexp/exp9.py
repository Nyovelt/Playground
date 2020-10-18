from physexp import *

a = [0.06, 0.063, 0.07, 0.068, 0.06, 0.063] #金属丝直径测量
print("初始数据平均值",Avg(a))
print("初始数据标准偏差",standardDeviationOfTheMean(a))
print("初始数据肖涅维法则剔粗差后结果",schauvignianCode(a))
b = schauvignianCode(a) #剔粗差
print("粗差后数据平均值",Avg(b))  
print("粗差后数据标准偏差",standardDeviationOfTheMean(b))
x_group = np.array([10,20,30,40,50,60,70,80,90,100,110])
y_group = np.array([1,1.425,1.9,2.3,2.7,3.1,3.5,3.925,4.325,4.775,5.175])
leastSquares(x_group, y_group, 0, 120, 10)