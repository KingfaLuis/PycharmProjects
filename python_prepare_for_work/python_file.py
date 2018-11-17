import os
import os.path
import shutil

# def visit_dir(path):
#     li = os.listdir(path)
#     for p in li:
#         pathname = os.path.join(path,p)
#         if not os.path.isfile(pathname):
#             visit_dir(pathname)
#         else:
#             print(pathname)

def visit_dit_2(arg,dirname,names):
    for filepath in names:
        print(os.path.join(dirname,filepath))

def del_file(path):
    '''
    删除文件
    :param path:
    :return:
    '''
    # file("hello.txt","w")
    if os.path.exists("hello.txt"):
        os.remove("hello.txt")

    return " "

def file_copy():
    shutil.copyfile("hello.txt","hello2.txt")
    # shutil.move("hello.txt","../")
    # shutil.move("hello2.txt","hello3.txt")
    return ""

def file_open():
    content = "hello world hello china"
    f = open("file_note.md",'w')
    open("README.md",'r')
    f.close()
    return ""

if __name__ == "__main__":
    # path = r"G:\Program Files\JetBrains\PyCharm 2018.2.1\bin"
    # visit_dir(path)
    # os.path.work(path,visit_dit_2,())

    # path = "G:\workspace\PycharmProjects\python_prepare_for_work\hell0.txt"
    path = "hello.txt"
    # del_file(path)
    # file_copy()
    file_open()
    open("README.md", 'r')


