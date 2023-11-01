# def fun(a):
#     b = a / (a - 1)
#
#     print("Value of b = ", b)
#
#
# try:
#     fun(int(input("enter number")))
#
#
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")

class coustom(Exception):
    pass
try:
    a=int(input("enter number"))
    if a==1:
        raise coustom
    else:print(a)
except:
    print("one cannot be entered")

