def add_matrices(a, b):

    result = [[0 for j in range(len(a[0]))] for i in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]

    return result


# Example usage.
a = int(input())
b = [[-1, 0], [2, -3]]

print("a =")
for row in a:
    print(row)

print("b =")
for row in b:
    print(row)

c = add_matrices(a, b)

print("a + b =")
for row in c:
    print(row)
