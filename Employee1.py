from Person import Person

class Employee1(Person):
    organizationName = "TCS" #class level variable

    def __init__(self, firstName, aadharNumber, gender, bloodGroup, empId, empCity):
        print("Employee 1 init block called")#object level variables
        super().__init__(firstName, aadharNumber, gender, bloodGroup)
        self.empId = empId
        self.empCity = empCity

    def __str__(self):
        super().__str__()
        return (f'{self.empId} '
                f'{self.empCity}')

emp = Employee1("Vrushali",
                "23232454546767",
                "female",
                "B+",
                12312,
                "Pune")
print(emp)