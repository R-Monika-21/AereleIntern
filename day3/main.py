#Day 3
"""
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
"""

from invoice import Invoice, InvoiceController

        

invoice1  = Invoice(invoice_number = "IN001", customer = "Monika", amount = 100.0, status = "Draft", paid = False)
print(invoice1)
controller = InvoiceController(invoice1)
controller.validate()
print("Invoice is valid")
print(invoice1.status)
controller.submit()
print(invoice1.status)

