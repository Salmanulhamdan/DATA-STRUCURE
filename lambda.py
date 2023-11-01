def exp(a):
    c = a * (a + 5) ** 2
    return c


print("user defind function",exp(5))

exp1 = lambda b: b * (b + 5) ** 2
print("lambda examble",exp1(6))
