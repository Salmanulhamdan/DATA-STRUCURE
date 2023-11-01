class maths:
    def __init__(self, no1, no2):
        self.num1 = no1
        self.num2 = no2

    def addition(self):
        print(self.num1 + self.num2)

    def substraction(self):
        print(self.num1 - self.num2)

    def mul(self):
        print(self.num1 * self.num2)

    def division(self):
        print(self.num1 / self.num2)


a = int(input("enter first number"))
b = int(input("enter seccond number"))
cal = maths(a, b)


def main():
    choice = int(input("choice1:sum\n choice2:substraction\n choice3:multiplication\n choice4:division "))
    if choice == 1:
        cal.addition()
    elif choice == 2:
        cal.substraction()
    elif choice == 3:
        cal.mul()
    elif choice == 4:
        cal.division()
    else:
        print("choice correct number")


main()
