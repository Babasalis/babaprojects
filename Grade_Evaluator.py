"""
Create a Student class with name, grades (a list),
 and a method that calculates their average grade and tells them if they passed or failed (pass mark is 50)
"""
class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        pass_mark = 50
        average = sum(self.grades)/len(self.grades)
        if average >= pass_mark:
            return f"You passed. Your average is {average:,.2f}"
        else:
            return f"You failed. Your average is {average:,.2f}"

karim = Student("Karim", [20,40.50,80,70,92])
print(karim.average_grade())
