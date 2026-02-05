class Employee:
    organizationName = "TCS" #class level variable

    def __init__(self,firstName,lastName,empId,empCity):        #object level variables
        self.firstName = firstName
        self.lastName = lastName
        self.empId = empId
        self.empCity = empCity

    def __str__(self):
        return (f'{self.firstName} '
                f'{self.lastName} '
                f'{self.empId} '
                f'{self.empCity}')

employee1 = Employee("Nikita",
                     "Abc",
                     23415,
                     "Pune")
print(employee1.organizationName)

employee2 = Employee("Vrushali",
                     "Abcd",
                     3412,
                     "Pune")
print(employee2.organizationName)
employee2.firstName = "Nikita"

#class level property can be changed by using classname.propertyName
Employee.organizationName = "Bitcode Technologies"

print(employee1.organizationName)
print(employee2.organizationName)