class Course:
    
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
        
    def average(self):
        numOfRatings=len(self.ratings)
        average=sum(self.ratings)/numOfRatings
        return average

c1=Course("Python",[1,2,3,4,5])
print(c1.name,c1.ratings)
print("Average rating of",c1.name ,"is", c1.average())

c2=Course("Java",[3,4,5])
print(c2.name,c2.ratings)
print("Average rating of",c2.name ,"is", c2.average())
