import random

def error_statement(a):
    try:
        print(a)
    except:
        a = 1
        print(a)
    else:
        print('rainy')
    finally:
        print('find job')

#实现单例模式
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls,*args,**kwargs)
        return cls._instance

class Myclass(Singleton):
    a = 1



if __name__ == "__main__":
    list = [1,2,3,3,4,5,5,6,5,7]
    a = set(list)
    print(a)
    error_statement(a)

    #写一个python中的单利模式
    one = Myclass()
    two = Myclass()
    # id(one) = id(two)

    b = 0.0
    print(bool(b))


