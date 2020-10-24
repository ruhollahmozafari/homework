#class for cars info.
class car():
    #attributes
    def __init__(self,name, model, color, year, mileage, speed,):
        self.__name=name
        self.__model= model
        self.__color= color
        self.__year= year
        self.__mileage= mileage
        self.__speed=speed
    #Getters for having access to properties
    def name_getter(self):
        return self.__name
    def model_getter(self):
        return self.__model
    def color_getter(self):
        return self.__color
    def year__getter(self):
        return self.__year
    def mileage_getter(self):
        return self.__mileage
    def speed_getter(self):
        return self.__speed
    
    #Setter to change the properties values
    def name_setter(self,name):
        return self.__name
    def model_setter(self, model):
        return self.__model
    def color_setter(self, color):
        return self.__color
    def year__setter(self, year):
        return self.__year
    def mileage_setter(self, mileage):
        return self.__mileage
    def speed_setter(self, speed):
        self.__speed = speed
        return self.__speed

porsche=car('porsche','carra','red', 2018, 0, 285 )
print(porsche.speed_getter())
print(porsche.speed_setter(300))
print(porsche.speed_getter())

