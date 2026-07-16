#Day 2
def generate_report(name, marks, total, avg, grade):
    with open(f"{name}_report.text", "w") as file:
        file.write(f"Report for {name}\n")
        file.write("Marks: \n")
        for i in range(len(marks)):
            file.write(f"Subject {i + 1} : {marks[i]}\n")
        file.write(f"Total marks: {total}\n")
        file.write(f"Average marks: {avg}\n")
        file.write(f"Grade: {grade}\n")
def calculate_total(marks):
    s = sum(marks)
    return s
def average(marks): 
    avg = sum(marks) / len(marks)
    return avg
def calculate_grade(avg):
    if avg >= 90:
        return "O"
    elif avg >= 80:
        return "A+"
    elif avg >= 70:
        return "A"
    elif avg >= 60:
        return "B+"
    elif avg >= 50:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"
name  = input("Enter your name: ")
num_of_subjects = int(input("Enter the number of subjects: "))
marks = []
for i in range(num_of_subjects):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)
total = calculate_total(marks)
avg = average(marks)
grade = calculate_grade(avg)
print(f"Total Marks: {total}\nAverage: {avg}")
print(f"Grade:{grade}")
generate_report(name, marks, total, avg, grade)

#Day 3
from dataclasses import dataclass
class A:
    def display(self):
        print("Display from A")
    
class B(A):
    def display(self):
        print("Display from B")
class C(A):
    def display(self):
        print("Display from C")
class D(C, B):
    pass
obj = D()
obj.display()
print("\nMRO:")
for cls in D.__mro__:
    print(cls.__name__)


@dataclass
class Student:
    name: str
    age: int
    marks: list

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "O"
        elif avg >= 80:
            return "A+"
        elif avg >= 70:
            return "A"
        elif avg >= 60:
            return "B+"
        elif avg >= 50:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "F"
student = Student(name="John Doe", age=20, marks=[85, 90, 78, 92])
total = student.calculate_total()
average = student.calculate_average()
grade = student.calculate_grade()
print(f"Total Marks: {total}\nAverage: {average}\nGrade: {grade}")

class StudentController:
    def __init__(self, student):
        self.student = student


