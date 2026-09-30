from student import Student

class StudentManager:
    def __init__(self):
        self.students=[]

    def add_student(self,name,marks):
        student=Student(name,marks)
        self.students.append(student)

    def view_students(self):
        for student in self.students:
            student.display()
    def search_student(self,name):
        for student in self.students:
            if student.name.lower()==name.lower():
                student.display()
                return
        print("student not found")
    def update_student(self,name,new_marks):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.set_marks(new_marks)
                print("Marks updated successfully")
                return
        print("student not found")

    def delete_student(self,name):
        for student in self.students:
            if student.name.lower()==name.lower():
                self.students.remove(student)
                print("student deleted successfully")
                return
        print("student deleted successfully")

        
