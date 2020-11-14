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

    def code(self):
        print(f"{self.name}is writing code"),

    def code_in_language(self,language):
        print(f"{self.name} codes in language {language}")

    #dunder method
    def __str__(self):
        information = f"name= {self.name}, age={self.age}, level={self.level}"
        return information

    def __eq__(self,other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if(age<25):
            return 5000
        if(age<30):
            return 7000
        return 9000
    


se1 = SoftwareEngineer( "Eren", 24, "Mid", 4000)
print(se1.age,se1.name) 
print(se1.alias)
print(SoftwareEngineer.alias)
se1.code()
se1.code_in_language("cpp")
# print(se1.information())
print(se1)

se2 = SoftwareEngineer( "Bico", 25, "Senior", 5000)
se3 = SoftwareEngineer( "Bico", 25, "Senior", 5000)
print(SoftwareEngineer.alias)
print(se3==se2)

print(se1.entry_salary(27))
print(SoftwareEngineer.entry_salary(24))

#Recap
#instance method itself
#can take arguments and return values
#special dunder method
#statismethod