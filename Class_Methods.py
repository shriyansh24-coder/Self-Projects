#Class Methods

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"

student1 = Student("Alice", 9.8)
student2 = Student("Bob", 8.5)
student3 = Student("Charlie", 7.9)

print(student1.get_info())  # Alice has a GPA of 9.8
print(student2.get_info())  # Bob has a GPA of 8.5
print(student3.get_info())  # Charlie has a GPA of 7.9

print(Student.get_count())  # Total number of students: 3    
print(Student.get_average_gpa())  # Average GPA: 8.73