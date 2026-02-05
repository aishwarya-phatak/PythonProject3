from Person import Person

class Student(Person):
    studentCount = 0            #class level attribute

    def __init__(self, firstName, aadharNumber, gender, bloodGroup, rollNumber, batchId, batchName):
        print("init of Student Class called")
        super().__init__(firstName, aadharNumber, gender, bloodGroup)
        self.rollNumber = rollNumber
        self.batchId = batchId
        self.batchName = batchName
        Student.studentCount += 1           #we can perform operations on class level attributes

    def __str__(self):
        print("str method of Student Class called")
        super().__str__()
        return (f'{self.rollNumber}   '
                f'{self.batchId}   '
                f'{self.batchName}  ')

    def displayDetails(self):
        print("display details method of Student Class called")
        super().displayDetails()

    @classmethod
    def studentCountDetails(cls):
        print("student count method of Student Class called")
        print("student count is : {}".format(cls.studentCount))

student1 = Student("Aishwarya","232345457878",
                   "Female","A+",
                   12314,45,"AI")

student2 = Student("Nikita","232345457878",
                   "Female","A+",
                   12334,45,"AI")

student3 = Student("Pallavi","232345457878",
                   "Female","A+",
                   1224,45,"AI")

print(student1)
student1.displayDetails()           #object specific method
Student.studentCountDetails()       #class method


