class SofwareEngineer:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self._salary = 5000
        self._num_of_bugs_solved = 0

    def code(self):
        self._num_of_bugs_solved +=1

    #getter
    def get_salary(self):
        return self._salary
 
    #setter
    def set_salary(self, base_value):
        #check value

        self._salary= self._calculate_salary(base_value)   

    def _calculate_salary(self,base_value):
        if self._num_of_bugs_solved < 10:
            return base_value
        if self._num_of_bugs_solved < 100:
            return base_value*2
        return base_value*3

se= SofwareEngineer("Eren", 24)
print(se.age, se.name, se._salary)

for i in range(33):
    se.code() 

se.set_salary(30030030)
print(se.get_salary())

