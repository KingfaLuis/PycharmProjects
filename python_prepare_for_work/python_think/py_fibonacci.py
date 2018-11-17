fibonacci = []
f0 = 0
f1 = 1
f2 = 1

# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return F(n-1) + F(n-2)

# startNumber = int(input("Enter the start number here "))
# endNumber = int(input("Enter the end number here "))
#
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-2) + fib(n-1)
#
# print(map(fib, range(startNumber, endNumber)))

# fibonacci = [0,1,1]
# def fib_p(n):
#     for n in range(n):
#         if n >= 2:
#             F = fibonacci
#             F.append(F[-1] + F[-2])
#         print(F)
# fib_p(range(endNumber))


def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b = b,a+b
    print()

def fib2(n):
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b, a+b
    return result
    print(result)

if __name__ == "__main__":
    fib(6)
    fib2(6)


