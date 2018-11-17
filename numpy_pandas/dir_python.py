import os
# import os.path
# import shutil

def visit_dir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path,p)
        if not os.path.isfile(pathname):
            visit_dir(pathname)
        else:
            print pathname

def visit_dit_2(arg,dirname,names):
    for filepath in names:
        print(os.path.join(dirname,filepath))

if __name__ == "__main__":
    path = r"G:\Program Files\JetBrains\PyCharm 2018.2.1\bin"
    # visit_dir(path)
    os.path.walk(path, visit_dit_2, ())