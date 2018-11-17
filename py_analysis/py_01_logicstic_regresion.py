# class A(object):
#     def show(self):
#         print('base show')
#
# class B(A):
#     def show(self):
#         print('derived show')

# obj = B()
# obj.show()
# obj.__class__
# 这个为什么会报错

#问题：为了让下面这段代码运行，需要增加哪些代码？
#这个题目，现在有什么问题？
#TypeError: 'A' object is not callable
#增加调用A的方法。
# class A(object):
#     def __init__(self,a,b):
#         self.__a = a
#         self.__b = b
#     def myprint(self):
#         print('a=',self.__a,'b=',self.__b)
#
#     # def __call__(self, *args, **kwargs):这两个参数
#     def __call__(self, *args, **kwargs):
#         print('call:',)

# a1=A(10,20)
# a1.myprint()
#
# a1()




'''
3、new和init
下面这段代码输出什么？
理解回答：限制性__new__,在执行__init__。从上往下顺序运行。

'''
class B(object):
    def fn(self):
        print('B fn')
    def __init__(self):
        print('B init')

class A(object):
    def fn(self):
        print('A fn')
    def __new__(cls, a):
        print('new',a)
        if a > 10:
            return super(A,cls).__new__(cls)
        return B()
    def __init__(self,a):
        print('inir',a)

a1 = A(5)
a1.fn()
a2 = A(20)
a2.fn()
'''
理解，使用new可以决定返回哪个对象。
'''

'''
4、Python list和dict生成
下面这段代码输出什么?
为什么选字典？
'''


ls = [1,2,3,4]
list1 = [i for i in ls if i>0]
print(list1)

list2 = [i*2 for i in ls if i>2]
print(list2)

dic1 = {x: x**2 for x in (2, 4, 6)}
print(dic1)

dic2 = {x: 'item' + str(x**2) for x in (2, 4, 6)}
print(dic2)

set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)


'''
# 全局和全局变量
下面这段代码输出什么?

在函数之外，不能访问局部变量，需要通过函数来引用。

num不是个全局变量，所以每个函数都得到了自己的num拷贝，
如果你想修改num，则必须用global关键字声明。比如下面这样
'''
num = 9

def f1():
    num = 20
    print(num)
def f2():
    global num
    print(num)

f2()
f1()
f2()
# 9
# 20
# 9

'''
6、交换两个变量的值
'''
a = 8
b = 9
print(a,b)
(a,b) = (b,a)
print(a,b)

'''
默认方法
'''
class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print('init')
    def mydefault(self):
        print('default')
# 添加代码
    def __getattr__(self, item):
        return self.mydefault
a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()

'''
8、包管理
一个包里有三个模块，mod1.py, mod2.py, mod3.py，
但使用from demopack import *导入模块时，
如何保证只有mod1、mod3被导入了。
'''

# __all__ = ['mod1','mod3']
'''
写一个函数，接收整数参数n，返回一个函数，
函数的功能是把函数的参数和n相乘并把结果返回。
'''
def mulby(num):
    def gn(val):
        return num * val

    return gn

zw = mulby(7)
print(zw(9))

def bibao(num):
    def getnum(vai):
        return num * vai
    return getnum

bb = bibao(8)
print(bb(9))

'''
10.性能
解析下面的代码慢在哪
'''
def strtest1(num):
    str='first'
    for i in range(num):
        str+="X"
    return str
print(strtest1(4))