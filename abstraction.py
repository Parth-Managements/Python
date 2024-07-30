from abc import ABC , abstractmethod

class Exampleclass(ABC):
    def disp(self):
        pass
    
    @abstractmethod
    def display(self):
        pass
    
class ChildClass(Exampleclass):
    def display(self):
        print("Parth")
        
        
obj = ChildClass()
obj.display()

        
