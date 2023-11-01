class Home:
    def _init_(self):
        pass

    def room1(self):
        width = 150
        breadth = 100
        print("Area of Room-1 is:", width*breadth)

    def room2(self):
        width = 140
        breadth = 100
        print("Area of Room-2 is:",width*breadth)

    def kitchen(self):
        width = 1500
        breadth = 5000
        print("Area of Kitchen is:",width*breadth)

class firsthome(Home):
    def _init_(self):
        super()._init_()

    def studyroom(self):
        width = 135
        breadth = 150
        print("Area of Study Room is:", width * breadth)

class secondhome(Home):
    def _init_(self):
        super()._init_()

    def workarea(self):
        width = 95
        breadth = 100
        print("Area of work area is:", width * breadth)

frsthome = firsthome()
frsthome.studyroom()
frsthome.room1()

secndhome = secondhome()
secndhome.workarea()
secndhome.kitchen()