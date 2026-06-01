class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def average(self):
        return sum(self.grade) / len(self.grade)

student_one = Student("Vivian", 25, [83, 90, 78, 92, 88])

print(f"{student_one.name}'s Average score is {student_one.average():.1f}")