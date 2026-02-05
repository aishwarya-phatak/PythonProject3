class Person:
    def __init__(self, firstName, aadharNumber, gender, bloodGroup):
        print("init of Person Class called")
        self.firstName = firstName
        self.aadharNumber = aadharNumber
        self.gender = gender
        self.bloodGroup = bloodGroup

    def __str__(self):
        print("str method of Person Class called")
        return (f'{self.firstName} '
                f'{self.aadharNumber} '
                f'{self.gender} '
                f'{self.bloodGroup}')

    def displayDetails(self):
        print("display details method of Person Class called")
        print("First Name : {} -- aadhar Number : {}".format(self.firstName, self.aadharNumber))
