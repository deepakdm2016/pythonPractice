from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):
    
    def __init__(self):
        super().__init__()
        print("Touch screen laptop")
        
    @abstractmethod
    def Scroll(self):
        pass
    
    @abstractmethod
    def Click(self):
        pass
    
class HP(TouchScreenLaptop):
    
    def __init__(self):
        super().__init__()
        print("HP laptop")
        
    
    def Scroll(self):
        print("Scroll HP laptop")
        
    
    @abstractmethod
    def Click(self):
        pass
        
class Dell(TouchScreenLaptop):
    
    def __init__(self):
        super().__init__()
        print("Dell laptop")
        
    
    def Scroll(self):
        print("Scroll Dell laptop")
        
    
    @abstractmethod
    def Click(self):
        pass
    
class HPNoteBook(HP):
    
    def __init__(self):
        super().__init__()
        print("In HP Notebook class")
        
    def Click(self):
        print("Click HP Notebook")

class DellNoteBook(Dell):
    
    def __init__(self):
        super().__init__()
        print("In Dell Notebook class")
        
    def Click(self):
        print("Click Dell Notebook")
        
        
hp=HPNoteBook()
hp.Click()
hp.Scroll()

dell=DellNoteBook()
dell.Scroll()
dell.Click()