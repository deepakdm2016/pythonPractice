class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
        
    def display(self):
        print("Student details are",self.id,self.name,self.marks)