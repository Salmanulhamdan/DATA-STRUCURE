class student:
    def __init__(self,name,id,no):

        self.student_name=name
        self.student_id=id
        self.roll_no=no
    def display(self):
        self.student_name="hamdan"
        self.student_id=10
        self.roll_no=2
        
obj=student
obj.display()
