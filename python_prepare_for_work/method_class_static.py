# -*- coding: utf-8 -*-

def data_structure():
    mylist = [1,2,3,4,'oh']
    mytuple = (1,2,'hello',(4,5))
    mydict = {'python':1,'java':2,'matlab':3,'R':4,'C++':5}
    myset = set(['Lu','Wei','Jiang','Li','Pan','Liu'])

    s1 = set

    print(mydict)
    print(mytuple)
    print(mydict)
    print(myset)

    return ''

def method_diff():
    return ""

class Date(object):
    '''
    定义:

    静态函数(@staticmethod): 即静态方法,主要处理与这个类的逻辑关联;

    类函数(@classmethod): 即类方法, 更关注于从类中调用方法, 而不是在实例中调用方法, 可以用作方法重载, 传入参数cls;

    成员函数: 实例的方法, 只能通过实例进行调用;

    具体应用:

    日期的方法, 可以通过实例化(__init__)进行数据输出, 传入参数self;

    可以通过类的方法(@classmethod)进行数据转换, 传入参数cls;

    可以通过静态方法(@staticmethod)进行数据验证;
    '''
    day = 0
    month = 0
    year = 0

    def __init__(self,day=0,month=0,year=0):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return "{0}*{1}*{2}".format(self.day,self.month,self.year)

    @classmethod
    def from_string(cls,date_as_string):
        day,month,year = map(int,date_as_string.split('-'))
        date1 = cls(day,month,year)

        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day,month,year = map(int,date_as_string.split('-'))

        return day <= 31 and month <= 12 and year <= 3999


def diff_variable():
    '''
    a=1,b=2不用中间变量交换a和b的值
    j加法或异或
    :return:
    '''
    a = 1
    b = 2

    a = a + b
    b = a - b
    a = a - b
    print('a = {0},b = {1}'.format(a,b))

    a = a ^ b
    b = a ^ b
    a = a ^ b
    print('a = {0},b = {1}'.format(a,b))
    return ''

######
def string_reverse1(string):
    return string[::-1]

def string_reverse2(string):
    t = list(string)
    l = len(t)
    for i,j in zip(range(l-1,0,-1),range(1//2)):
        t[i],t[j] = t[j],t[i]
    return "".join(t)

from collections import deque

def string_reverse3(string):
    d = deque()
    d.extendleft(string)
    return "".join(d)

def string_reverse4(string):
    d = deque()
    d.extendleft(string)
    return ''.join(d)

def string_reverse5(string):
    return ''.join(string[i] for i in range(len(string)-1,-1,-1))

###

import random
def qsort(L):
    if len(L)<2:
        return L
    pivot_element = random.choice(L)
    small = [i for i in L if i<pivot_element]
    large = [i for i in L if i>pivot_element]
    return qsort(small) + [pivot_element] + qsort(large)

def list_merge(list1,list2):

    return qsort(list1 + list2)




if __name__ == "__main__":
    data_structure()

    #2.静态函数，类函数，成员函数的区别
    date1 = Date('19','8','2018')
    date2 = Date.from_string('8-19-2018')
    print(date1.display())
    print(date2.display())
    print(date2.is_date_valid('8-19-2018'))
    print(Date.is_date_valid('8-19-2018'))

    #a=1,b=2不用中间变量交换a和b的值
    diff_variable()

    # 逆序输出字符串的方法
    string = "abcdefgh"
    string_reverse1(string)
    print(string_reverse1(string))
    print(string_reverse2(string))
    print(string_reverse3(string))
    print(string_reverse4(string))
    print(string_reverse5(string))

    #5.请用自己的算法，按升序合并如下两个list，并去除重复的元素
    list1 = [3,41,3,5,8,10,33]
    list2 = [5,35,12,7,6,11,22]
    qsort(list1)
    qsort(list2)
    list_merge(list1,list2)
    print(list_merge(list1,list2))

    # 6.写出打印的结果
    x = [0,1]
    i = 0
    i,x[i] = 1,2
    print(x)
    # python 可以使用连续赋值，从左到右

    # g = lambda x,y=2,z: x + y **z
    # g(1,z=10)






