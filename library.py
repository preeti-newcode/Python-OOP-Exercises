#Library Management System
from abc import ABC,abstractmethod

class LibraryItem(ABC):
    
    @abstractmethod
    def displayInfo(self):
        pass
    
    @abstractmethod
    def borrowItems(self):
        pass

class book(LibraryItem):
    __title=["The Lost City","The Princess Diaries","The Coffeehouse Mystery","Echoes of Eternity","The Harry Potter"]
    __author=["Conan Doyle","Meg Cabot","Cleo Coyle","Rithesh Prakash","J.K. Rowling"]
    __available=5
    
    def displayInfo(self):
        if self.__available==0:
            print("No Book available")
            break
        
        for x in range(len(self.__title)):
            print(x,"\t","Author Name:",self.__author[x],"\tTitle:",self.__title[x])
            
    
    def borrowItems(self):
        print()
        x=int(input("Enter its Number you want to borrow:"))
        print(self.__title[x],"written by",self.__author[x],"given successfully")
        self.__available-=1 
        self.__title.pop(x)
        self.__author.pop(x)
        print()
        
#Main Body
x=book()
x.displayInfo()
x.borrowItems()
x.displayInfo()
