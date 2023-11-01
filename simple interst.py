def interst(p,n,r):
    i=(p*n*r)/100
    return i

p= float(input("enter your principle amount"))
n=int(input("enter your time period"))
r=float(input("enter the rate of intrest"))
print("your intrest is",interst(p,n,r))