se1=[ "Software Engineer", "Eren", "24", "Mid", "4000"]
se2=[ "Software Engineer", "Bico", "25", "Senior", "5000"]

class SoftwareEngineer:

    #class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

se1 = SoftwareEngineer( "Eren", 24, "Mid", 4000)
print(se1.age,se1.name)
print(se1.alias)
print(SoftwareEngineer.alias)

se2 = SoftwareEngineer( "Bico", 25, "Senior", 5000)
print(SoftwareEngineer.alias)

#Recap
#create a class (blueprint)
#create an instance (object)
#class vs instance
#instance attributes: defined in __init__(self)
#class attribute
