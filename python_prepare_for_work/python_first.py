# -* -coding: utf -8 -* -
#! /usr/bin/python
from keyword import kwlist
# import sys
from sys import path
from sys import argv
# import buildin


print(kwlist)
l = len(kwlist)
print(l)

# Fill this in with an expression that calculates how many tiles are needed.
need_tiles = 9*7 + 5*7
print(need_tiles)

# Fill this in with an expression that calculates how many tiles will be left over.
def left_tile(need_tiles):
    total_tiles = 17*6
    left_tiles = total_tiles - need_tiles
    print(left_tiles)
    return left_tiles

class Student:
    __name = ""
    def __init__(self,name):
        self.__name = name
    def getName(self):
        return self.__name

def compare_num(num1,num2):
    '''
    function: comapre
    :param num1:
    :param num2:
    :return:
    '''
    if(num1 > num2):
        return str(num1)+" > "+str(num2)
    elif (num1 < num2):
        return str(num1)+" < "+str(num2)
    elif (num1 == num2):
        return str(num1)+" = "+str(num2)
    else:
        return " "

def if_statement(score):
    if(score > 90) and (score <= 100):
        print("A")
    elif (score > 80) and (score <= 00):
        print("B")
    elif (score > 70) and (score <= 80):
        print("C")
    elif (score > 60) and (score <= 70):
        print("D")
    else:
        print("E")

def bubbleSort(numbers):
    for j in range(len(numbers) - 1, -1, -1):
        for i in range(j):
            if numbers[i] > numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            print(numbers)

def sum(x=1,y=3):
    return x + y

def refunc(n):
    '''
    递归函数计算阶乘
    :param n:
    :return:
    '''
    i = 1
    if n > 1:
        i = n
        n = n * refunc(n - 1)
    print(n)
    return n

def func_lambda():
    '''
    lambda表达式，不能使用判断，循环等多重语句
    :return:
    '''
    x = 1
    y = 2
    m = 3
    n = 4
    num = lambda x,y:x+y
    print(num)

def func_generator(n):
    for i in range(n):
        yield i

def func_diff_yield_return(n):
    for i in range(n):
        return i

def func_diff_yield_return_2(n):
    for i in range(n):
        yield i



if __name__ == "__main__":
    print('hello world')
    b = left_tile
    print(b)
    student = Student("Kingfaluis")
    print(student.getName())

    # print(sys.path)
    # print(sys.argv)
    print(path)
    print(argv)

    print(compare_num(2, 1))
    print(compare_num(2, 2))
    print(compare_num(2, 3))

    #冒泡排序实例
    numbers = [11,3,4,55,6]
    bubbleSort(numbers)

    # print(apply(sum,(1,3)))
    #
    # print(reduce(sum,range(0,10)))

    refunc(5) # 递归

    func_lambda()

    # func_generator(3)
    for i in func_generator(3):
        print(i)
    r = func_generator(3)
    # print(r.text())
    # print(r.text())
    # print(r.text())
    # print(r.text())

    print(func_diff_yield_return(3))
    f = func_diff_yield_return_2(3)
    print(f)
    print(f.text())
    print(f.text())














