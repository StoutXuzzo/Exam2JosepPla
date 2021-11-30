class BaseModel():
    def __init__(self,dni,name,surname):
        self.__dni = dni
        self.__name = name
        self.__surname = surname
    
    def getDNI(self):
        return self.__dni
    
    def getName(self):
        return self.__name
    
    def getSurname(self):
        return self.__surname
    
    def __str__(self):
        return self.__surname + ", " + self.__name + " : " + self.__dni
     