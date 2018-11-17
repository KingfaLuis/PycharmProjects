# -*- coding: utf-8 -*-
# class WithoutDecorators:
#     def some_static_method(self):
#         print("this is static method")
#     some_static_method = staticmethod(some_static_method)
#
#     def some_class_method(self):
#         print("this is class method")
#     some_class_method = classmethod(some_class_method)

class WithDecoratots:
    @staticmethod
    def some_static_method():
        print("this is static method")

    @classmethod
    def some_class_method(cls):
        print("this is class method")


def mydecorator(function):
    '''
    作为一个函数
    :param function:
    :return:
    '''
    def wrapped(*args,**kwargs):
        #在调用原始函数之前，做点什么
        result = function(*args,**kwargs)
        # 在函数调用之后，做点什么
        # 并返回结果
        return result
    #返回wrapper作为装饰函数
    return wrapped

class DecoratorAsClass:
    '''
    作为一个类
    :return:
    '''
    def __init__(self,function):
        self.function = function

    def __call__(self,*args,**kwargs):
        # 在调用函数之前，做点什么
        result = self.function(*args,**kwargs)
        # 在调用函数之后，做点什么
        # 并返回结果
        return result

def repeat(number=3):
    '''
    多次重复执行装饰函数
    返回最后一次原始函数调用的值作为结果
    :param number: 重复次数，默认值是3
    :return:
    '''
    def actual_decorator(function):
        def wrapper(*args,**kwargs):
            result = None
            for _ in range(number):
                result = function(*args,**kwargs)
            return result
        return wrapper
    return actual_decorator

if __name__ == "__main__":
    @repeat(2)
    def foo():
        print("foo")

    foo()

    @repeat()
    def bar():
        print("bar")
    bar()

    # 参数检查
    