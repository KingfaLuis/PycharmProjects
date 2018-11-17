# import os
def add(num):
    num = num + 10
    return num

def change(num):
    num.append(1)


if __name__ == "__main__":
    d = 2 #不可变对象
    add(d)
    print(d)

    d = [0] #可变对象
    change(d)
    print(d)

    d = 2
    d = add(d) #创建新的对象
    print(d)

    squares = [x**2 for x in range(9)]
    print(squares)
    print(sum(squares))

    num_2 = [x for x in range(10) if x % 2 == 0]
    print(num_2)

    nested_list = [[0 for x in range(10)] for y in range(10)]
    print(nested_list)

    # dict_comprehension = {k: v**3 for (k,v) in zip(str.islower(),range(26))}
    # print(dict_comprehension)