class Student:
    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id
    
    def setName(self,name):
        self.name=name
        
    def getName(self):
        return self.name


s=Student()
s.setId(389524)
s.setName("Deepak")

print(s.getId(),s.getName())


