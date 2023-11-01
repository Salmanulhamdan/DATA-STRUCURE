print("enter the mark scored by student")
w = float(input("written test"))
l = float(input("lab exam"))
a = float(input("assignments"))


def w_avg():
    avg = ((w * 70) / 100 + (l * 20) / 100 + (a * 10) / 100)
    print("Grade of the student is",avg)


w_avg()
