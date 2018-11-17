# # from amodule import *
#
# class dummyclass(object):
#     def __init__(self):
#         self.is_d = True
#         pass
#
#
# class childdummyclass(dummyclass):
#     def __init__(self, isman):
#         self.isman = isman
#
#     @classmethod
#     def can_speak(self): return True
#
#     @property
#     def man(self): return self.isman
#
#
# if __name__ == "__main__":
#     object1 = new
#     #没有关键字new
#     childdummyclass(True)
#     print
#     object1.can_speak()
#     print
#     object1.man()

class dummyclass(object):
    def __init__(self):
        self.is_d = True
        pass


class childdummyclass(dummyclass):
    def __init__(self, isman):
        dummyclass.__init__(self)  # __init__
        self.isman = isman

    @classmethod
    def can_speak(cls): return True  # cls

    @property
    def man(self): return self.isman


if __name__ == "__main__":
    o = childdummyclass(True)  # new, object
    print(o.can_speak())
    print(o.man)   # property
    print(o.is_d)


