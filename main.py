from Employee1 import Employee1
from Person import Person
from Student import Student

#polymorphism - run time binding
def introduce(person):
    person.displayDetails()

personObj = Person("Pallavi","454523236767",
                   "Female","B+")

studentObj1 = Student("Nikita","4542356767","Female",
                      "A+",2387,98,"AI")

studentObj2 = Student("Snehal","909067678989","Female",
                      "AB+",67543,76,"AI")

introduce(personObj)
introduce(studentObj1)
introduce(studentObj2)

print(" {}".format(isinstance(personObj, Person)))
print(" {}".format(isinstance(studentObj1, Student)))
print(" {}".format(isinstance(studentObj2, Person)))
print(" {}".format(isinstance(studentObj2, Employee1)))