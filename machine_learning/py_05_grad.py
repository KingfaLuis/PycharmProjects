# _*_ coding: utf-8 _*_
def train(X, y, W, B, alpha, max_iters):
    '''
    使用了所有的样本进行梯度下降
    X: 训练集,
    y: 标签,
    W: 权重向量,
    B: bias,
    alpha: 学习率,
    max_iters: 最大迭代次数.
    '''
    dW = 0 # 权重梯度收集器
    dB = 0 # Bias梯度的收集器
    m = X.shape[0] # 样本数
    for i in range(max_iters):
        dW = 0 # 每次迭代重置
        dB = 0
        for j in range(m):
            # 1. 迭代所有的样本
            # 2. 计算权重和bias的梯度保存在w_grad和b_grad,
            # 3. 通过增加w_grad和b_grad来更新dW和dB
            W = W - alpha * (dW / m) # 更新权重
            B = B - alpha * (dB / m) # 更新bias

    return W, B




# 博客: http://blog.csdn.net/yhao2014


# 训练集
# 每个样本点有3个分量 (x0,x1,x2)
x = [(1, 0., 3), (1, 1., 3), (1, 2., 3), (1, 3., 2), (1, 4., 4)]
# y[i] 样本点对应的输出
y = [95.364, 97.217205, 75.195834, 60.105519, 49.342380]

# 迭代阀值，当两次迭代损失函数之差小于该阀值时停止迭代
epsilon = 0.0001

# 学习率
alpha = 0.01
diff = [0, 0]
max_itor = 1000
error1 = 0
error0 = 0
cnt = 0
m = len(x)

# 初始化参数
theta0 = 0
theta1 = 0
theta2 = 0

while True:
    cnt += 1

    # 参数迭代计算
    for i in range(m):
        # 拟合函数为 y = theta0 * x[0] + theta1 * x[1] +theta2 * x[2]
        # 计算残差
        diff[0] = (theta0 + theta1 * x[i][1] + theta2 * x[i][2]) - y[i]

        # 梯度 = diff[0] * x[i][j]
        theta0 -= alpha * diff[0] * x[i][0]
        theta1 -= alpha * diff[0] * x[i][1]
        theta2 -= alpha * diff[0] * x[i][2]

    # 计算损失函数
    error1 = 0
    for lp in range(len(x)):
        error1 += (y[lp] - (theta0 + theta1 * x[lp][1] + theta2 * x[lp][2])) ** 2 / 2

    if abs(error1 - error0) < epsilon:
        break
    else:
        error0 = error1

    print
    ' theta0 : %f, theta1 : %f, theta2 : %f, error1 : %f' % (theta0, theta1, theta2, error1)
print
'Done: theta0 : %f, theta1 : %f, theta2 : %f' % (theta0, theta1, theta2)
print
'迭代次数: %d' % cnt
