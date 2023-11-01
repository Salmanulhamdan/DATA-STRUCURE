# a=input("enter  a charecter")
# print("entered char=", a)
def a(v):
    def c():
        print("fsadf")
        v()
    return c
@a
def k():
    print("fdf")
k()