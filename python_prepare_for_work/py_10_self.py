'''
本例子的参考链接
https://blog.csdn.net/CLHugh/article/details/75000104
'''
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s" % (self.name,self.score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score = score

    def get_grade(self):
        '''
        封装的好处是可以随时给student类增加新的方法
        :return:
        '''
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        else:
            return 'C'

class Test:
    '''

    '''
    def ppr(self):
        '''
        self可以不写吗？
        不可以
        :return:
        '''
        print(self)
        return {
            "url": url,
            "name":name,
            "rating":rating,
            "address":address,
            "phone":duration,
            "introduction":introduction

        }


if __name__ == "__main__":
    student = Student('KingfaLu',99)
    student.name
    student.score

    print(student.get_grade())

    # 测试省去self会发生错误
    t = Test()
    print(t.ppr())



