def get_array():
    size = int(input("enter the size of array"))
    print("enter values")
    for i in range(size):
        array.append(int(input()))


def display_array():
    print(array)


def main():
    global array
    array = []
    get_array()
    display_array()


main()
