class Programmer:
    
    major="Developer"
    def setName(self,n):
        self.name=n
    
    def getName(self):
        return self.name
    
    def setSalary(self,sal):
        self.salary=sal
    
    def getSalary(self):
        return self.salary    
    
    def setTechnologies(self,technologies):
        self.technologies=technologies
    
    def getTechnologies(self):
        return self.technologies
    
    def display(self):
        print(self.name,self.salary,self.technologies,Programmer.major)
    
p1=Programmer()
p1.setName("Deepak")
p1.setSalary("10000")
p1.setTechnologies(["Java","RestWS","Python","Hibernate"])

p1.display()