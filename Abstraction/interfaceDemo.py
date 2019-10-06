from abc import abstractmethod,ABC

class Car(ABC):
    
    def __init__(self,model,year):
        self.model=model
        self.year=year
    
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def park(self):
        pass
    
    
class Ferrari(Car):
    
    def __init__(self, model, year, speed):
        Car.__init__(self, model, year)
        self.speed=speed
        
    def drive(self):
        print("This car drives at speed of ",self.speed)
        
    
    def park(self):
        print("Ferrari is automatic parking enabled")
        

f=Ferrari("I20",2019,450)
f.drive()
f.park()