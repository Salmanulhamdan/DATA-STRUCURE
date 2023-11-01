class stack:
    def __init__(self):
        self.data=[]
    def push(self,data):
        self.data.append(data)
    def pop(self):
        return self.data.pop()

    def display(self):
        return self.data
s1=stack()
s1.push(5)
s1.push(6)
s1.push(4)
s1.push(3)
print(s1.display())
s1.pop()
s1.pop()
print(s1.display())