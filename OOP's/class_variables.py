class Student:

    clas_year = 2025
    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = Student("Anu",21)

print(student1.name)
print(student1.age)
print(Student.clas_year)  #class variable
