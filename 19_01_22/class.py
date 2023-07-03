# class

class Person:
    #class attributes
    address = "no information"
    #constructor (yapıcı metod)
    def __init__(self, name, year):
        #object attributes
        self.name = name
        self.birthyear = year 
        print("init metodu çalıştı")
        #methods 


#object (instane)
p1 = Person()