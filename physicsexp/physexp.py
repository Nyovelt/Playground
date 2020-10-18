import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as op


def Avg(arr:list):
    ret = 0
    for i in arr:
        ret += i
    return ret / len(arr)

def standardDeviation(arr:list):
    avg = Avg(arr)
    ret = 0
    for i in arr:
        ret += (i-avg)**2
    ret = ret ** 0.5
    return ret

def standardDeviationOfTheMean(arr:list):
    n = len(arr)
    return standardDeviation(arr)/(n*(n-1))**0.5

def schauvignianCode(arr: list): 
    s = standardDeviationOfTheMean(arr) #sigma
    c = 1.75 
    ret = []
    for i in arr:
        if(abs(i - Avg(arr)) >= c*s):
            continue
        else:
            ret.append(i)
    return ret



# 需要拟合的函数
def f_1(x, A, B):
    return A * x + B

def leastSquares(x_group:list, y_group:list, start, end, delta):
    # 得到返回的A，B值
    A, B = op.curve_fit(f_1, x_group, y_group)[0]
    # 数据点与原先的进行画图比较
    plt.scatter(x_group, y_group, marker='o',label='real')
    x = np.arange(start, end, delta)
    y = A * x + B
    plt.plot(x, y,color='red',label='curve_fit')
    plt.legend()
    plt.title('%.5fx%+-.5f=y' % (A, B))
    plt.show()
    plt.savefig("leastSquares.png")
 
