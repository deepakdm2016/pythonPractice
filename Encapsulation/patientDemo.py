class Patient:
    def setId(self,id):
        self.id=id
        
    def getId(self):
        return self.id
    
    def setName(self,name):
        self.name=name
        
    def getName(self):
        return self.name
    
    def setSSN(self,ssn):
        self.ssn=ssn
        
    def getSSN(self):
        return self.ssn
    
p1=Patient()
p1.setId(389524)
p1.setName("Deepak")
p1.setSSN("123-34-4354")
    
print(p1.getId(),p1.getName(),p1.getSSN())
    
    
    